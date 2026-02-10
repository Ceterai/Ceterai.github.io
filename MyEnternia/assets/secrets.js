// Secret Easter Eggs System
(function() {
    'use strict';
    
    const SECRETS_KEY = 'myEnterniaSecretsFound';
    const SECRET_MESSAGE = '🗝️ You found a hidden treasure...';
    
    // Secret page URLs that count as discoveries (edit this list to add more)
    const SECRET_PAGES = [
        'xfw8uf',
        'ceteraisstardust',
        'asirai',
        'companiondrone'
    ];
    
    // Calculate total: 3 fixed secrets (s1=uwu, s2=box, s3=trail) + SECRET_PAGES
    const TOTAL_SECRETS = 3 + SECRET_PAGES.length;
    
    // Get found secrets
    function getFoundSecrets() {
        try {
            return JSON.parse(localStorage.getItem(SECRETS_KEY) || '[]');
        } catch (e) {
            return [];
        }
    }
    
    // Save found secrets
    function saveFoundSecrets(secrets) {
        try {
            localStorage.setItem(SECRETS_KEY, JSON.stringify(secrets));
        } catch (e) {}
    }
    
    // Check if secret is already found
    function isSecretFound(secretId) {
        return getFoundSecrets().includes(secretId);
    }
    
    // Mark secret as found and show notification
    function discoverSecret(secretId) {
        if (isSecretFound(secretId)) {
            return false; // Already found
        }
        
        const secrets = getFoundSecrets();
        secrets.push(secretId);
        saveFoundSecrets(secrets);
        
        // Update stats if tracking is available
        if (window.myEnterniaStats) {
            window.myEnterniaStats.updateSecretCount();
        }
        
        // Show notification
        showSecretNotification(SECRET_MESSAGE);
        
        return true;
    }
    
    // Show secret discovery notification
    function showSecretNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'secret-notification';
        notification.innerHTML = `
            <div class="secret-notification-content">
                <div class="secret-sparkle">✨</div>
                <div class="secret-message">${message}</div>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => notification.classList.add('show'), 100);
        
        // Remove after 4 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 500);
        }, 4000);
    }
    
    // UwU-ifier
    function uwuifyText(text) {
        return text
            .replace(/[rl]/g, 'w')
            .replace(/[RL]/g, 'W')
            .replace(/n([aeiou])/g, 'ny$1')
            .replace(/N([aeiou])/g, 'Ny$1')
            .replace(/N([AEIOU])/g, 'NY$1')
            .replace(/ove/g, 'uv')
            .replace(/!+/g, '!~ òωó ')
            .replace(/\.\.\./g, '~ ^ω^')
            .replace(/…/g, '~ oωo')
            .replace(/\.$/g, '~ uωu')
            .replace(/\.[^a-zA-Z0-9]/g, '~ ≥ω≤ ');
    }
    
    let uwuActive = false;
    const originalTexts = new Map();
    
    function toggleUwuMode() {
        uwuActive = !uwuActive;
        
        if (uwuActive) {
            // UwU-ify all text nodes
            const walker = document.createTreeWalker(
                document.querySelector('.ct_body'),
                NodeFilter.SHOW_TEXT,
                null
            );
            
            let node;
            while (node = walker.nextNode()) {
                if (node.textContent.trim() && !node.parentElement.closest('script, style, code, pre')) {
                    originalTexts.set(node, node.textContent);
                    node.textContent = uwuifyText(node.textContent);
                }
            }
            
            discoverSecret('s1');
        } else {
            // Restore original text
            originalTexts.forEach((original, node) => {
                node.textContent = original;
            });
            originalTexts.clear();
        }
    }
    
    // Cursor trail effect
    let trailActive = false;
    
    function createTrailParticle(x, y) {
        const particle = document.createElement('div');
        particle.className = 'cursor-trail';
        particle.style.left = x + 'px';
        particle.style.top = y + 'px';
        particle.innerHTML = ['✨', '⭐', '💫', '🌟'][Math.floor(Math.random() * 4)];
        document.body.appendChild(particle);
        
        setTimeout(() => particle.remove(), 1000);
    }
    
    function toggleCursorTrail() {
        trailActive = !trailActive;
        
        if (trailActive) {
            discoverSecret('s3');
            document.addEventListener('mousemove', handleTrailMove);
        } else {
            document.removeEventListener('mousemove', handleTrailMove);
        }
    }
    
    function handleTrailMove(e) {
        if (trailActive && Math.random() > 0.7) {
            createTrailParticle(e.pageX, e.pageY);
        }
    }
    
    // Typing detector for secret word
    let typedChars = '';
    const SECRET_WORD = 'ceterai';
    
    function handleTyping(e) {
        // Don't trigger in input fields or search page
        if (e.target.matches('input, textarea') || window.location.pathname.includes('/search')) {
            return;
        }
        
        typedChars += e.key.toLowerCase();
        
        // Keep only last 10 chars
        if (typedChars.length > 10) {
            typedChars = typedChars.slice(-10);
        }
        
        // Check if secret word was typed
        if (typedChars.includes(SECRET_WORD)) {
            typedChars = '';
            window.location.href = '/MyEnternia/Wiki/xFw8Uf/';
        }
    }
    
    // Mystery box spawner (1% chance)
    function spawnMysteryBox() {
        if (Math.random() > 0.01) return; // 1% chance
        
        const box = document.createElement('div');
        box.className = 'mystery-box';
        box.innerHTML = '❓';
        box.title = 'What could this be?';
        
        // Random horizontal position (10% to 90% of width)
        const randomPos = 10 + Math.random() * 80;
        box.style.left = `${randomPos}%`;
        
        box.addEventListener('click', () => {
            discoverSecret('s2');
            box.classList.add('clicked');
            setTimeout(() => box.remove(), 500);
        });
        
        // Insert before footer
        const footer = document.querySelector('.ct_body > :last-child');
        if (footer) {
            footer.before(box);
        } else {
            document.querySelector('.ct_body').appendChild(box);
        }
    }
    
    // Check for secret pages
    function checkSecretPages() {
        const path = window.location.pathname.toLowerCase();
        
        // Check each secret page in the list
        SECRET_PAGES.forEach((page, index) => {
            if (path.includes(page)) {
                // s4, s5, s6, s7 are for secret pages (s3 is trail)
                discoverSecret(`s${index + 4}`);
            }
        });
    }
    
    // Expose API
    window.myEnterniaSecrets = {
        discover: discoverSecret,
        isFound: isSecretFound,
        getFoundCount: () => getFoundSecrets().length,
        getTotalCount: () => TOTAL_SECRETS,
        reset: () => {
            localStorage.removeItem(SECRETS_KEY);
            if (window.myEnterniaStats) {
                window.myEnterniaStats.updateSecretCount();
            }
        }
    };
    
    // Initialize
    function init() {
        if (!window.location.pathname.includes('/MyEnternia/')) return;
        
        // Check for secret pages
        checkSecretPages();
        
        // Setup Alt+U shortcut for UwU mode
        document.addEventListener('keydown', (e) => {
            if (e.altKey && e.key === 'u' && !e.ctrlKey && !e.shiftKey) {
                e.preventDefault();
                toggleUwuMode();
            }
            
            // Setup Alt+T shortcut for cursor trail
            if (e.altKey && e.key === 't' && !e.ctrlKey && !e.shiftKey) {
                e.preventDefault();
                toggleCursorTrail();
            }
        });
        
        // Setup typing detector
        document.addEventListener('keypress', handleTyping);
        
        // Spawn mystery box (1% chance)
        if (window.location.pathname.includes('/MyEnternia/Wiki/')) {
            spawnMysteryBox();
        }
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
