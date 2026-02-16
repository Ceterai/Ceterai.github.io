// Back to Top Button
(function() {
    'use strict';
    
    // Create back to top button
    function createBackToTopButton() {
        const backToTopBtn = document.createElement('div');
        backToTopBtn.className = 'back-to-top-badge';
        backToTopBtn.innerHTML = `
            <button class="back-to-top-btn" title="Back to top">
                ↑
            </button>
        `;
        
        document.body.appendChild(backToTopBtn);
        
        // Scroll to top on click
        const btn = backToTopBtn.querySelector('.back-to-top-btn');
        btn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
        // Show on scroll
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            backToTopBtn.classList.add('visible');
            
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                if (window.scrollY < 100) {
                    backToTopBtn.classList.remove('visible');
                }
            }, 3000);
        });
        
        // Show if already scrolled
        if (window.scrollY > 100) {
            backToTopBtn.classList.add('visible');
        }
    }
    
    // Initialize
    function init() {
        const path = window.location.pathname;
        // Show on all pages except the site root page
        if (path === '/' || path === '/index.html') return;
        
        createBackToTopButton();
    }
    
    window.MyEnterniaUtils.onDOMReady(init);
})();
