// View Counter for Wiki Pages
// Tracks your personal exploration of the wiki using localStorage
(function() {
    'use strict';
    
    const PERSONAL_VIEWS_KEY = 'myEnterniaPersonalViews';
    const EXTRA_STATS_KEY = 'myEnterniaExtraStats';
    
    // Get personal view tracking (localStorage)
    function getPersonalViews() {
        try {
            return JSON.parse(localStorage.getItem(PERSONAL_VIEWS_KEY) || '{}');
        } catch (e) {
            return {};
        }
    }
    
    // Save personal views
    function savePersonalViews(views) {
        try {
            localStorage.setItem(PERSONAL_VIEWS_KEY, JSON.stringify(views));
        } catch (e) {}
    }
    
    // Get/set extra stats (link clicks, random uses, easter eggs)
    function getExtraStats() {
        try {
            return JSON.parse(localStorage.getItem(EXTRA_STATS_KEY) || '{"linksClicked":0,"randomUsed":0,"easterEggs":0}');
        } catch (e) {
            return { linksClicked: 0, randomUsed: 0, easterEggs: 0 };
        }
    }
    
    function saveExtraStats(stats) {
        try {
            localStorage.setItem(EXTRA_STATS_KEY, JSON.stringify(stats));
        } catch (e) {}
    }
    
    // Expose a global helper so other scripts can bump stats
    window.myEnterniaStats = {
        trackLinkClick: function() {
            const s = getExtraStats();
            s.linksClicked++;
            saveExtraStats(s);
        },
        trackRandomPage: function() {
            const s = getExtraStats();
            s.randomUsed++;
            saveExtraStats(s);
        },
        trackEasterEgg: function() {
            const s = getExtraStats();
            s.easterEggs++;
            saveExtraStats(s);
        }
    };
    
    // Get bookmark count from bookmarks localStorage
    function getBookmarkCount() {
        try {
            return JSON.parse(localStorage.getItem('myEnterniaBookmarks') || '[]').length;
        } catch (e) {
            return 0;
        }
    }
    
    // Check if this is user's first time viewing this page
    function checkFirstView(url) {
        return !getPersonalViews()[url];
    }
    
    // Mark page as personally viewed and return count
    function markAsPersonallyViewed(url) {
        const views = getPersonalViews();
        if (!views[url]) {
            views[url] = { firstView: Date.now(), viewCount: 0 };
        }
        views[url].viewCount++;
        views[url].lastView = Date.now();
        savePersonalViews(views);
        return views[url].viewCount;
    }
    
    // Get personal stats
    function getPersonalStats() {
        const views = getPersonalViews();
        const pages = Object.keys(views).length;
        const total = Object.values(views).reduce((sum, v) => sum + v.viewCount, 0);
        const extra = getExtraStats();
        const bookmarks = getBookmarkCount();
        return { pages, total, linksClicked: extra.linksClicked, randomUsed: extra.randomUsed, bookmarks, easterEggs: extra.easterEggs };
    }
    
    // Track wiki link clicks
    function setupLinkTracking() {
        document.addEventListener('click', (e) => {
            const link = e.target.closest('a[href*="/MyEnternia/Wiki/"]');
            if (link && !link.closest('.bookmarks-menu') && !link.closest('#wiki-tools')) {
                window.myEnterniaStats.trackLinkClick();
            }
        });
    }
    
    // Initialize view counter
    function initViewCounter() {
        if (!window.location.pathname.includes('/MyEnternia/Wiki/')) return;
        
        const toolsBar = document.getElementById('wiki-tools');
        if (!toolsBar) return;
        
        const url = window.location.pathname;
        const firstView = checkFirstView(url);
        const viewCount = markAsPersonallyViewed(url);
        const stats = getPersonalStats();
        
        // Create compact view counter button
        const counter = document.createElement('button');
        counter.className = 'wiki-tool-btn view-counter-btn';
        counter.innerHTML = firstView ? '👁️ 1 ✨' : `👁️ ${viewCount}`;
        counter.title = firstView 
            ? 'Your first time on this page!' 
            : `You've visited this page ${viewCount} time${viewCount !== 1 ? 's' : ''}`;
        
        // Create stats wrapper with dropdown
        const statsWrapper = document.createElement('div');
        statsWrapper.className = 'bookmarks-menu-wrapper';
        statsWrapper.innerHTML = `
            <button class="wiki-tool-btn" id="stats-toggle" title="Your exploration stats">📊</button>
            <div class="view-stats-dropdown" id="stats-dropdown">
                <div class="stats-header">Your Exploration</div>
                <div class="stats-item">
                    <span class="stats-label">Total visits:</span>
                    <span class="stats-value">${stats.total.toLocaleString()}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">Pages explored:</span>
                    <span class="stats-value">${stats.pages.toLocaleString()}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">This page:</span>
                    <span class="stats-value">${viewCount.toLocaleString()}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">Links clicked:</span>
                    <span class="stats-value">${stats.linksClicked.toLocaleString()}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">Random pages:</span>
                    <span class="stats-value">${stats.randomUsed.toLocaleString()}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">Bookmarks:</span>
                    <span class="stats-value">${stats.bookmarks.toLocaleString()}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">Easter eggs:</span>
                    <span class="stats-value">${stats.easterEggs.toLocaleString()}</span>
                </div>
                <button class="reset-stats">Reset Stats</button>
            </div>
        `;
        
        toolsBar.appendChild(counter);
        toolsBar.appendChild(statsWrapper);
        
        // Stats toggle
        statsWrapper.querySelector('#stats-toggle').addEventListener('click', (e) => {
            e.stopPropagation();
            statsWrapper.querySelector('#stats-dropdown').classList.toggle('show');
        });
        
        // Close dropdown on outside click
        document.addEventListener('click', (e) => {
            if (!statsWrapper.contains(e.target)) {
                statsWrapper.querySelector('#stats-dropdown').classList.remove('show');
            }
        });
        
        // Reset button
        statsWrapper.querySelector('.reset-stats').addEventListener('click', () => {
            if (confirm('Reset your exploration stats?')) {
                localStorage.removeItem(PERSONAL_VIEWS_KEY);
                localStorage.removeItem(EXTRA_STATS_KEY);
                location.reload();
            }
        });
        
        // Track wiki link clicks
        setupLinkTracking();
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initViewCounter);
    } else {
        initViewCounter();
    }
})();
