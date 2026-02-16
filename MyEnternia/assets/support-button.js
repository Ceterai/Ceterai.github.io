// Support Button - Buy Me a Coffee & Ko-fi
(function() {
    'use strict';
    
    // Create floating support badge
    function createFloatingBadge() {
        const badge = document.createElement('div');
        badge.className = 'support-badge';
        badge.innerHTML = `
            <button class="support-btn" title="Support my work">
                ☕ Support
            </button>
            <div class="support-popup">
                <div class="support-header">Support Ceterai</div>
                <a href="https://buymeacoffee.com/ceterai" target="_blank" rel="noopener" class="support-link bmc">
                    <span class="support-icon">☕</span>
                    <span class="support-label">Buy Me a Coffee</span>
                </a>
                <a href="https://ko-fi.com/ceterai" target="_blank" rel="noopener" class="support-link kofi">
                    <span class="support-icon">💙</span>
                    <span class="support-label">Ko-fi</span>
                </a>
            </div>
        `;
        
        document.body.appendChild(badge);
        
        // Show on scroll
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            badge.classList.add('visible');
            
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                if (window.scrollY < 100) {
                    badge.classList.remove('visible');
                }
            }, 3000);
        });
        
        // Show if already scrolled
        if (window.scrollY > 100) {
            badge.classList.add('visible');
        }
    }
    
    // Add to stats dropdown
    function addToStatsDropdown() {
        const statsDropdown = document.getElementById('stats-dropdown');
        if (!statsDropdown) return;
        
        const supportItem = document.createElement('div');
        supportItem.className = 'stats-support-item';
        supportItem.innerHTML = `
            <div class="support-message">
                💙 Enjoying the wiki?
            </div>
            <div class="support-popup-wrapper">
                <button class="support-inline-btn">
                    ☕ Support Ceterai
                </button>
                <div class="support-popup support-popup-inline">
                    <a href="https://buymeacoffee.com/ceterai" target="_blank" rel="noopener" class="support-link bmc">
                        <span class="support-icon">☕</span>
                        <span class="support-label">Buy Me a Coffee</span>
                    </a>
                    <a href="https://ko-fi.com/ceterai" target="_blank" rel="noopener" class="support-link kofi">
                        <span class="support-icon">💙</span>
                        <span class="support-label">Ko-fi</span>
                    </a>
                </div>
            </div>
        `;
        
        // Insert before reset button
        const resetBtn = statsDropdown.querySelector('.reset-stats');
        if (resetBtn) {
            resetBtn.before(supportItem);
        }
    }
    
    // Initialize
    function init() {
        const path = window.location.pathname;
        // Show on all pages except the site root page
        if (path === '/' || path === '/index.html') return;
        
        createFloatingBadge();
        
        // Wait for stats dropdown to be created
        setTimeout(addToStatsDropdown, 1000);
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        // Delay slightly to ensure DOM is fully settled
        setTimeout(init, 0);
    }
})();
