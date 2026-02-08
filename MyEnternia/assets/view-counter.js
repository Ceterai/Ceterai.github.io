// View Counter for Wiki Pages
// Using counterapi.dev for global view tracking + localStorage for personal stats
(function() {
    'use strict';
    
    const API_BASE = 'https://api.counterapi.dev/v1';
    const NAMESPACE = 'ceterai-myenternia';
    const PERSONAL_VIEWS_KEY = 'myEnterniaPersonalViews';
    const TIMEOUT_MS = 4000;
    
    // Convert URL to safe key format
    function urlToKey(url) {
        return url.replace(/[^a-zA-Z0-9]/g, '_').substring(0, 64);
    }
    
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
    
    // Check if this is user's first time viewing this page
    function checkFirstView(url) {
        return !getPersonalViews()[url];
    }
    
    // Mark page as personally viewed
    function markAsPersonallyViewed(url) {
        const views = getPersonalViews();
        if (!views[url]) {
            views[url] = { firstView: Date.now(), viewCount: 1 };
        } else {
            views[url].viewCount++;
        }
        views[url].lastView = Date.now();
        savePersonalViews(views);
    }
    
    // Fetch with timeout
    function fetchWithTimeout(url, ms) {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), ms);
        return fetch(url, { signal: controller.signal }).finally(() => clearTimeout(timeout));
    }
    
    // Increment global view count via API
    async function incrementGlobalViewCount(url) {
        try {
            const key = urlToKey(url);
            const response = await fetchWithTimeout(`${API_BASE}/${NAMESPACE}/${key}/up`, TIMEOUT_MS);
            const data = await response.json();
            return data.count || 0;
        } catch (e) {
            console.warn('View counter API unavailable, using local count');
            return null;
        }
    }
    
    // Get personal stats
    function getPersonalStats() {
        const views = getPersonalViews();
        const pages = Object.keys(views).length;
        const total = Object.values(views).reduce((sum, v) => sum + v.viewCount, 0);
        return { pages, total };
    }
    
    // Format number
    function fmt(n) {
        if (n === null || n === undefined) return '?';
        return n.toLocaleString();
    }
    
    // Initialize view counter
    async function initViewCounter() {
        if (!window.location.pathname.includes('/MyEnternia/Wiki/')) return;
        
        const toolsBar = document.getElementById('wiki-tools');
        if (!toolsBar) return;
        
        const url = window.location.pathname;
        const firstView = checkFirstView(url);
        
        // Create compact view counter button
        const counter = document.createElement('button');
        counter.className = 'wiki-tool-btn view-counter-btn';
        counter.innerHTML = '👁️ …';
        counter.title = 'Page views (loading...)';
        
        // Create stats wrapper with dropdown
        const statsWrapper = document.createElement('div');
        statsWrapper.className = 'bookmarks-menu-wrapper';
        
        const stats = getPersonalStats();
        statsWrapper.innerHTML = `
            <button class="wiki-tool-btn" id="stats-toggle" title="Your personal stats">📊</button>
            <div class="view-stats-dropdown" id="stats-dropdown">
                <div class="stats-header">Your Stats</div>
                <div class="stats-item">
                    <span class="stats-label">Your visits:</span>
                    <span class="stats-value">${fmt(stats.total)}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">Pages explored:</span>
                    <span class="stats-value">${fmt(stats.pages)}</span>
                </div>
                <div class="stats-note">View counts are shared across all visitors</div>
                <button class="reset-stats">Reset Personal Stats</button>
            </div>
        `;
        
        toolsBar.appendChild(counter);
        toolsBar.appendChild(statsWrapper);
        
        // Stats toggle
        const toggleBtn = statsWrapper.querySelector('#stats-toggle');
        const dropdown = statsWrapper.querySelector('#stats-dropdown');
        
        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdown.classList.toggle('show');
        });
        
        // Close dropdown on outside click
        document.addEventListener('click', (e) => {
            if (!statsWrapper.contains(e.target)) {
                dropdown.classList.remove('show');
            }
        });
        
        // Reset button
        statsWrapper.querySelector('.reset-stats').addEventListener('click', () => {
            if (confirm('Reset your personal statistics?')) {
                localStorage.removeItem(PERSONAL_VIEWS_KEY);
                location.reload();
            }
        });
        
        // Fetch global count (with timeout so it doesn't hang forever)
        const globalCount = await incrementGlobalViewCount(url);
        
        // Update counter display
        if (globalCount !== null) {
            counter.innerHTML = `👁️ ${fmt(globalCount)}`;
            counter.title = `${fmt(globalCount)} total views`;
        } else {
            // Fallback to personal view count
            const personal = getPersonalViews()[url];
            const localCount = personal ? personal.viewCount + 1 : 1;
            counter.innerHTML = `👁️ ${fmt(localCount)}`;
            counter.title = `${fmt(localCount)} of your views (global counter unavailable)`;
        }
        
        // First view sparkle
        if (firstView) {
            counter.innerHTML += ' ✨';
            counter.title += ' — First visit!';
        }
        
        // Mark as viewed
        markAsPersonallyViewed(url);
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initViewCounter);
    } else {
        initViewCounter();
    }
})();
