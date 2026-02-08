// View Counter for Wiki Pages
// Using CountAPI.xyz for global view tracking across all visitors
(function() {
    'use strict';
    
    const API_BASE = 'https://api.countapi.xyz';
    const NAMESPACE = 'ceterai-myenternia';
    const PERSONAL_VIEWS_KEY = 'myEnterniaPersonalViews';
    
    // Convert URL to safe key format
    function urlToKey(url) {
        return url.replace(/[^a-zA-Z0-9-_]/g, '_').substring(0, 64);
    }
    
    // Get personal view tracking (localStorage)
    function getPersonalViews() {
        try {
            const views = localStorage.getItem(PERSONAL_VIEWS_KEY);
            return views ? JSON.parse(views) : {};
        } catch (e) {
            console.error('Error reading personal views:', e);
            return {};
        }
    }
    
    // Save personal views
    function savePersonalViews(views) {
        try {
            localStorage.setItem(PERSONAL_VIEWS_KEY, JSON.stringify(views));
        } catch (e) {
            console.error('Error saving personal views:', e);
        }
    }
    
    // Check if this is user's first time viewing this page
    function isFirstView(url) {
        const views = getPersonalViews();
        return !views[url];
    }
    
    // Mark page as personally viewed
    function markAsPersonallyViewed(url) {
        const views = getPersonalViews();
        if (!views[url]) {
            views[url] = {
                firstView: Date.now(),
                viewCount: 1
            };
        } else {
            views[url].viewCount++;
        }
        views[url].lastView = Date.now();
        savePersonalViews(views);
    }
    
    // Get global view count from API
    async function getGlobalViewCount(url) {
        try {
            const key = urlToKey(url);
            const response = await fetch(`${API_BASE}/get/${NAMESPACE}/${key}`);
            const data = await response.json();
            return data.value || 0;
        } catch (e) {
            console.error('Error fetching view count:', e);
            return null;
        }
    }
    
    // Increment global view count via API
    async function incrementGlobalViewCount(url) {
        try {
            const key = urlToKey(url);
            const response = await fetch(`${API_BASE}/hit/${NAMESPACE}/${key}`);
            const data = await response.json();
            return data.value || 0;
        } catch (e) {
            console.error('Error incrementing view count:', e);
            return null;
        }
    }
    
    // Get personal stats
    function getPersonalStats() {
        const views = getPersonalViews();
        const pages = Object.keys(views).length;
        const totalPersonal = Object.values(views).reduce((sum, v) => sum + v.viewCount, 0);
        return { pages, totalPersonal };
    }
    
    // Format number with comma separators
    function formatNumber(num) {
        if (num === null) return '...';
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    }
    
    // Create view counter element
    function createViewCounter(globalCount, isFirstView) {
        const counter = document.createElement('div');
        counter.className = 'view-counter';
        
        if (globalCount === null) {
            counter.innerHTML = `
                <div class="view-counter-item">
                    <span class="view-icon">👁️</span>
                    <span class="view-count">Loading...</span>
                </div>
            `;
        } else {
            counter.innerHTML = `
                <div class="view-counter-item">
                    <span class="view-icon">👁️</span>
                    <span class="view-count">${formatNumber(globalCount)}</span>
                    <span class="view-label">view${globalCount !== 1 ? 's' : ''}</span>
                    ${isFirstView ? '<span class="first-view-badge" title="Your first time here!">✨</span>' : ''}
                </div>
            `;
        }
        
        if (isFirstView) {
            counter.classList.add('first-view');
        }
        
        return counter;
    }
    
    // Create stats panel
    function createStatsPanel() {
        const stats = getPersonalStats();
        
        const panel = document.createElement('div');
        panel.className = 'view-stats-panel';
        panel.innerHTML = `
            <button class="view-stats-toggle" title="View your personal statistics">
                📊 <span>Your Stats</span>
            </button>
            <div class="view-stats-dropdown">
                <div class="stats-header">Personal Stats</div>
                <div class="stats-item">
                    <span class="stats-label">Your views:</span>
                    <span class="stats-value">${formatNumber(stats.totalPersonal)}</span>
                </div>
                <div class="stats-item">
                    <span class="stats-label">Pages explored:</span>
                    <span class="stats-value">${formatNumber(stats.pages)}</span>
                </div>
                <div class="stats-note">Global view counts are shared across all visitors via CountAPI</div>
                <button class="reset-stats" title="Reset your personal statistics">Reset Personal Stats</button>
            </div>
        `;
        
        return panel;
    }
    
    // Initialize view counter
    async function initViewCounter() {
        // Only initialize on Wiki pages
        if (!window.location.pathname.includes('/MyEnternia/Wiki/')) {
            return;
        }
        
        const url = window.location.pathname;
        const isFirstView = isFirstView(url);
        
        // Create view counter with loading state
        const viewCounter = createViewCounter(null, isFirstView);
        
        // Create stats panel
        const statsPanel = createStatsPanel();
        
        // Insert into the wiki-tools bar
        const toolsBar = document.getElementById('wiki-tools');
        if (toolsBar) {
            toolsBar.appendChild(viewCounter);
            toolsBar.appendChild(statsPanel);
        }
        
        // Fetch and update global count
        const globalCount = await incrementGlobalViewCount(url);
        
        // Update view counter with actual count
        if (globalCount !== null) {
            const counterItem = viewCounter.querySelector('.view-counter-item');
            if (counterItem) {
                counterItem.innerHTML = `
                    <span class="view-icon">👁️</span>
                    <span class="view-count">${formatNumber(globalCount)}</span>
                    <span class="view-label">view${globalCount !== 1 ? 's' : ''}</span>
                    ${isFirstView ? '<span class="first-view-badge" title="Your first time here!">✨</span>' : ''}
                `;
            }
        }
        
        // Mark as personally viewed
        markAsPersonallyViewed(url);
        
        // Setup stats toggle
        const toggleBtn = statsPanel.querySelector('.view-stats-toggle');
        const dropdown = statsPanel.querySelector('.view-stats-dropdown');
        
        toggleBtn.addEventListener('click', () => {
            dropdown.classList.toggle('show');
        });
        
        // Setup reset button
        const resetBtn = statsPanel.querySelector('.reset-stats');
        resetBtn.addEventListener('click', () => {
            if (confirm('Are you sure you want to reset your personal statistics? (This will not affect global view counts)')) {
                localStorage.removeItem(PERSONAL_VIEWS_KEY);
                location.reload();
            }
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!statsPanel.contains(e.target)) {
                dropdown.classList.remove('show');
            }
        });
        
        // Show special animation for first view
        if (isFirstView && globalCount !== null) {
            setTimeout(() => {
                viewCounter.classList.add('celebrate');
                setTimeout(() => {
                    viewCounter.classList.remove('celebrate');
                }, 1000);
            }, 300);
        }
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initViewCounter);
    } else {
        initViewCounter();
    }
})();
