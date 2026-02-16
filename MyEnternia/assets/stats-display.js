/**
 * Stats Display UI
 * 
 * Shows exploration stats in the wiki toolbar:
 * - View counter badge
 * - Stats dropdown menu with detailed statistics
 * - Integration with view-counter, bookmarks, and secrets
 * 
 * Dependencies: utils.js, view-counter.js
 * Provides: window.myEnterniaStatsDisplay API
 */
(function() {
    'use strict';
    
    // Create view counter badge
    function createViewCounterBadge() {
        if (!window.myEnterniaStats) return null;
        
        const viewCount = window.myEnterniaStats.getCurrentPageViewCount();
        const firstView = viewCount === 1;
        
        const counter = document.createElement('button');
        counter.className = 'wiki-tool-btn view-counter-btn';
        counter.innerHTML = firstView ? '👁️ 1 ✨' : `👁️ ${viewCount}`;
        counter.title = firstView 
            ? 'Your first time on this page!' 
            : `You've visited this page ${viewCount} time${viewCount !== 1 ? 's' : ''}`;
        
        return counter;
    }
    
    // Create stats dropdown
    function createStatsDropdown() {
        if (!window.myEnterniaStats) return null;
        
        const stats = window.myEnterniaStats.getPersonalStats();
        const viewCount = window.myEnterniaStats.getCurrentPageViewCount();
        
        const statsWrapper = document.createElement('div');
        statsWrapper.className = 'bookmarks-menu-wrapper';
        statsWrapper.innerHTML = `
            <button class="wiki-tool-btn" id="stats-toggle" title="Your exploration stats">📊</button>
            <div class="view-stats-dropdown" id="stats-dropdown">
                <div class="bookmarks-menu-header">
                    <h3>Your Exploration</h3>
                    <button class="close-menu" title="Close">×</button>
                </div>
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
                    <span class="stats-label">Secrets:</span>
                    <span class="stats-value">${stats.secretsFound}/${stats.secretsTotal}</span>
                </div>
                <button class="reset-stats">Reset Stats</button>
            </div>
        `;
        
        // Stats toggle
        statsWrapper.querySelector('#stats-toggle').addEventListener('click', (e) => {
            e.stopPropagation();
            statsWrapper.querySelector('#stats-dropdown').classList.toggle('show');
        });
        
        // Close button
        statsWrapper.querySelector('.close-menu').addEventListener('click', () => {
            statsWrapper.querySelector('#stats-dropdown').classList.remove('show');
        });
        
        // Close dropdown on outside click
        document.addEventListener('click', (e) => {
            if (!statsWrapper.contains(e.target)) {
                statsWrapper.querySelector('#stats-dropdown').classList.remove('show');
            }
        });
        
        // Reset button
        statsWrapper.querySelector('.reset-stats').addEventListener('click', () => {
            if (confirm('Reset your exploration stats? (This will NOT reset discovered secrets)')) {
                window.myEnterniaStats.resetStats();
                location.reload();
            }
        });
        
        return statsWrapper;
    }
    
    // Update stats dropdown with current values
    function updateStatsDropdown() {
        const dropdown = document.getElementById('stats-dropdown');
        if (!dropdown || !window.myEnterniaStats) return;
        
        const stats = window.myEnterniaStats.getPersonalStats();
        const secretValue = dropdown.querySelector('.stats-item:last-of-type .stats-value');
        if (secretValue) {
            secretValue.textContent = `${stats.secretsFound}/${stats.secretsTotal}`;
        }
    }
    
    // Initialize stats display
    function initStatsDisplay() {
        if (!window.MyEnterniaUtils.isWikiPage()) return;
        
        const toolsBar = document.getElementById('wiki-tools');
        if (!toolsBar) return;
        
        const counter = createViewCounterBadge();
        const statsDropdown = createStatsDropdown();
        
        if (counter) toolsBar.appendChild(counter);
        if (statsDropdown) toolsBar.appendChild(statsDropdown);
    }
    
    // Expose update method for other scripts (like secrets)
    window.myEnterniaStatsDisplay = {
        updateSecretCount: updateStatsDropdown
    };
    
    window.MyEnterniaUtils.onDOMReady(initStatsDisplay);
})();
