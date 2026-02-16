/**
 * View Counter & Stats Tracking for Wiki Pages
 * 
 * Tracks user's personal exploration of the wiki using localStorage:
 * - Page view counts per URL
 * - Total visits and unique pages explored
 * - Link clicks, random page uses
 * - Integration with bookmarks and secrets systems
 * 
 * Dependencies: utils.js
 * Provides: window.myEnterniaStats API
 */
(function() {
    'use strict';
    
    const PERSONAL_VIEWS_KEY = 'myEnterniaPersonalViews';
    const EXTRA_STATS_KEY = 'myEnterniaExtraStats';
    
    // Get personal view tracking (localStorage)
    const getPersonalViews = () => window.MyEnterniaUtils.getFromStorage(PERSONAL_VIEWS_KEY, {});
    
    // Save personal views
    const savePersonalViews = (views) => window.MyEnterniaUtils.saveToStorage(PERSONAL_VIEWS_KEY, views);
    
    // Get/set extra stats (link clicks, random uses, easter eggs)
    const getExtraStats = () => window.MyEnterniaUtils.getFromStorage(EXTRA_STATS_KEY, {linksClicked: 0, randomUsed: 0, easterEggs: 0});
    
    const saveExtraStats = (stats) => window.MyEnterniaUtils.saveToStorage(EXTRA_STATS_KEY, stats);
    
    // Get bookmark count from bookmarks localStorage
    const getBookmarkCount = () => window.MyEnterniaUtils.getFromStorage('myEnterniaBookmarks', []).length;
    
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
        if (!window.MyEnterniaUtils.isWikiPage()) return;
        
        const url = window.location.pathname;
        markAsPersonallyViewed(url);
        
        // Track wiki link clicks
        setupLinkTracking();
    }
    
    window.MyEnterniaUtils.onDOMReady(initViewCounter);
})();
