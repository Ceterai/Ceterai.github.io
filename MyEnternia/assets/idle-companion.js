// Idle Companion - Narfin Pet Animation
(function() {
    'use strict';
    
    const IDLE_TIMEOUT = 30000; // 30 seconds of inactivity
    let idleTimer = null;
    let companionActive = false;
    let companion = null;
    
    // Narfin sprite frames (using emoji/unicode as placeholder - can be replaced with actual images)
    const NARFIN_SPRITE = '🦊'; // Fox emoji as placeholder
    
    function createCompanion() {
        if (companion) return;
        
        companion = document.createElement('div');
        companion.className = 'idle-companion narfin';
        companion.innerHTML = `
            <div class="companion-sprite">${NARFIN_SPRITE}</div>
            <div class="companion-bubble">Looking for something?</div>
        `;
        companion.style.cssText = `
            position: fixed;
            bottom: -100px;
            right: 40px;
            z-index: 9999;
            cursor: pointer;
            transition: bottom 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            pointer-events: all;
        `;
        
        // Click to dismiss
        companion.addEventListener('click', hideCompanion);
        
        document.body.appendChild(companion);
        
        // Add styles
        if (!document.getElementById('companion-styles')) {
            const style = document.createElement('style');
            style.id = 'companion-styles';
            style.textContent = `
                .idle-companion {
                    text-align: center;
                }
                
                .companion-sprite {
                    font-size: 48px;
                    animation: companion-float 3s ease-in-out infinite;
                    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
                }
                
                .companion-bubble {
                    position: absolute;
                    bottom: 60px;
                    right: -20px;
                    background: rgba(100, 181, 246, 0.95);
                    color: white;
                    padding: 8px 12px;
                    border-radius: 12px;
                    font-size: 12px;
                    white-space: nowrap;
                    opacity: 0;
                    animation: bubble-appear 0.3s ease-out 0.5s forwards;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
                }
                
                .companion-bubble::after {
                    content: '';
                    position: absolute;
                    bottom: -6px;
                    right: 30px;
                    width: 0;
                    height: 0;
                    border-left: 6px solid transparent;
                    border-right: 6px solid transparent;
                    border-top: 6px solid rgba(100, 181, 246, 0.95);
                }
                
                @keyframes companion-float {
                    0%, 100% {
                        transform: translateY(0) rotate(-5deg);
                    }
                    50% {
                        transform: translateY(-10px) rotate(5deg);
                    }
                }
                
                @keyframes bubble-appear {
                    from {
                        opacity: 0;
                        transform: translateY(10px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                
                .idle-companion:hover .companion-sprite {
                    animation: companion-wave 0.5s ease-in-out;
                }
                
                @keyframes companion-wave {
                    0%, 100% { transform: rotate(-5deg); }
                    25% { transform: rotate(15deg); }
                    75% { transform: rotate(-15deg); }
                }
            `;
            document.head.appendChild(style);
        }
        
        // Slide in
        setTimeout(() => {
            companion.style.bottom = '20px';
            companionActive = true;
        }, 100);
        
        // Auto-hide bubble after 5 seconds
        setTimeout(() => {
            const bubble = companion.querySelector('.companion-bubble');
            if (bubble) {
                bubble.style.animation = 'none';
                bubble.style.opacity = '0';
            }
        }, 5000);
    }
    
    function hideCompanion() {
        if (!companion || !companionActive) return;
        
        companion.style.bottom = '-100px';
        companionActive = false;
        
        setTimeout(() => {
            if (companion && companion.parentNode) {
                companion.parentNode.removeChild(companion);
                companion = null;
            }
        }, 500);
    }
    
    function resetIdleTimer() {
        // Clear existing timer
        if (idleTimer) {
            clearTimeout(idleTimer);
        }
        
        // Hide companion if active
        if (companionActive) {
            hideCompanion();
        }
        
        // Start new timer
        idleTimer = setTimeout(() => {
            createCompanion();
        }, IDLE_TIMEOUT);
    }
    
    // Track user activity
    const activityEvents = ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart', 'click'];
    
    activityEvents.forEach(event => {
        document.addEventListener(event, resetIdleTimer, { passive: true });
    });
    
    // Initialize only on MyEnternia pages
    if (window.location.pathname.includes('/MyEnternia/')) {
        // Start idle timer on page load
        resetIdleTimer();
        
        console.log('🦊 Narfin companion is watching for idle time...');
    }
})();
