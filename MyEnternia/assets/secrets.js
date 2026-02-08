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
    
    // Calculate total: 2 fixed secrets (s1=uwu, s2=box) + SECRET_PAGES
    const TOTAL_SECRETS = 2 + SECRET_PAGES.length;
    
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
                // s3, s4, s5, s6 are for secret pages
                discoverSecret(`s${index + 3}`);
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
        
        // Setup Alt+U shortcut
        document.addEventListener('keydown', (e) => {
            if (e.altKey && e.key === 'u') {
                e.preventDefault();
                toggleUwuMode();
            }
        });
        
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
