// View Counter & Stats Tracking for Wiki Pages
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
        const secretsFound = window.myEnterniaSecrets ? window.myEnterniaSecrets.getFoundCount() : 0;
        const secretsTotal = window.myEnterniaSecrets ? window.myEnterniaSecrets.getTotalCount() : "?";
        return { pages, total, linksClicked: extra.linksClicked, randomUsed: extra.randomUsed, bookmarks, secretsFound, secretsTotal };
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
    
    // Expose global API for other scripts
    window.myEnterniaStats = {
        // Tracking methods
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
        
        // Data getters
        getPersonalStats: getPersonalStats,
        checkFirstView: checkFirstView,
        getCurrentPageViewCount: function() {
            const views = getPersonalViews();
            const url = window.location.pathname;
            return views[url] ? views[url].viewCount : 0;
        },
        
        // Reset
        resetStats: function() {
            localStorage.removeItem(PERSONAL_VIEWS_KEY);
            localStorage.removeItem(EXTRA_STATS_KEY);
        }
    };
    
    // Initialize view counter (track current page)
    function initViewCounter() {
        if (!(window.location.pathname + '/').includes('/MyEnternia/Wiki/')) return;
        
        console.log('Initializing view counter for', window.location.pathname);
        const url = window.location.pathname;
        markAsPersonallyViewed(url);
        
        // Track wiki link clicks
        setupLinkTracking();
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initViewCounter);
    } else {
        // Delay slightly to ensure DOM is fully settled
        setTimeout(initViewCounter, 0);
    }
})();
