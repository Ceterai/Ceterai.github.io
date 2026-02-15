// Text Glitch Effect for Special Keywords
(function() {
    'use strict';
    
    // Keywords that should glitch (with exact matching)
    const GLITCH_KEYWORDS = [
        { pattern: /\bC\.T\.\b/g, text: 'C.T.' },
        { pattern: /\bc\.t\.\b/g, text: 'c.t.' },
        { pattern: /\bmiazma\b/gi, text: 'miazma' }
    ];
    
    // Check if page path suggests glitchy content
    function isGlitchyPage() {
        const path = window.location.pathname.toLowerCase();
        return path.includes('ct_') || 
               path.includes('miazma') || 
               document.body.innerText.toLowerCase().includes('miazma');
    }
    
    // Wrap text nodes with glitch effect
    function applyGlitchEffect(element) {
        const walker = document.createTreeWalker(
            element,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode: function(node) {
                    // Skip script, style, and already processed nodes
                    const parent = node.parentElement;
                    if (!parent || 
                        parent.tagName === 'SCRIPT' || 
                        parent.tagName === 'STYLE' ||
                        parent.classList.contains('glitch-text') ||
                        parent.classList.contains('glitching') ||
                        parent.closest('.breadcrumb-bar') ||
                        parent.closest('nav') ||
                        parent.closest('.breadcrumb-left') ||
                        parent.closest('.breadcrumb-right')) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    return NodeFilter.FILTER_ACCEPT;
                }
            }
        );
        
        const nodesToProcess = [];
        let node;
        while (node = walker.nextNode()) {
            nodesToProcess.push(node);
        }
        
        nodesToProcess.forEach(textNode => {
            let modified = false;
            let html = textNode.textContent;
            
            // Check each keyword with proper word boundaries
            GLITCH_KEYWORDS.forEach(({ pattern, text }) => {
                if (pattern.test(html)) {
                    // Reset pattern index for next use
                    pattern.lastIndex = 0;
                    html = html.replace(pattern, (match) => {
                        modified = true;
                        return `<span class="glitch-text" data-text="${match}">${match}</span>`;
                    });
                }
            });
            
            if (modified) {
                const wrapper = document.createElement('span');
                wrapper.innerHTML = html;
                textNode.parentNode.replaceChild(wrapper, textNode);
            }
        });
    }
    
    // Random glitch animation
    function animateGlitches() {
        const glitchElements = document.querySelectorAll('.glitch-text');
        glitchElements.forEach(el => {
            if (Math.random() < 0.1) { // 10% chance per interval
                el.classList.add('glitching');
                setTimeout(() => el.classList.remove('glitching'), 200);
            }
        });
    }
    
    // Initialize on wiki pages
    if (window.location.pathname.includes('/MyEnternia/')) {
        // Wait for content to load
        setTimeout(() => {
            // Only apply to main content, avoid navigation/breadcrumbs
            const content = document.querySelector('main') || 
                            document.querySelector('article') || 
                            document.querySelector('.markdown-body');
            
            if (content) {
                applyGlitchEffect(content);
            }
            
            // Add CSS if not present
            if (!document.getElementById('glitch-styles')) {
                const style = document.createElement('style');
                style.id = 'glitch-styles';
                style.textContent = `
                    .glitch-text {
                        position: relative;
                        display: inline-block;
                        color: #00ffff;
                        text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
                        animation: glitch-subtle 3s infinite;
                    }
                    
                    .glitch-text.glitching {
                        animation: glitch-intense 0.2s;
                    }
                    
                    @keyframes glitch-subtle {
                        0%, 100% { 
                            text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
                        }
                        50% { 
                            text-shadow: 
                                -1px 0 2px rgba(255, 0, 255, 0.5),
                                1px 0 2px rgba(0, 255, 255, 0.5);
                        }
                    }
                    
                    @keyframes glitch-intense {
                        0% {
                            transform: translate(0);
                            text-shadow: 
                                -2px 0 5px rgba(255, 0, 0, 0.8),
                                2px 0 5px rgba(0, 255, 255, 0.8);
                        }
                        20% {
                            transform: translate(-2px, 1px);
                            text-shadow: 
                                2px 0 5px rgba(255, 0, 255, 0.8),
                                -2px 0 5px rgba(0, 255, 0, 0.8);
                        }
                        40% {
                            transform: translate(-2px, -1px);
                            text-shadow: 
                                -2px 0 5px rgba(0, 255, 255, 0.8),
                                2px 0 5px rgba(255, 255, 0, 0.8);
                        }
                        60% {
                            transform: translate(2px, 1px);
                            text-shadow: 
                                2px 0 5px rgba(255, 0, 0, 0.8),
                                -2px 0 5px rgba(0, 0, 255, 0.8);
                        }
                        80% {
                            transform: translate(1px, -1px);
                            text-shadow: 
                                -2px 0 5px rgba(255, 0, 255, 0.8),
                                2px 0 5px rgba(0, 255, 255, 0.8);
                        }
                        100% {
                            transform: translate(0);
                            text-shadow: 
                                -2px 0 5px rgba(255, 0, 0, 0.8),
                                2px 0 5px rgba(0, 255, 255, 0.8);
                        }
                    }
                `;
                document.head.appendChild(style);
            }
            
            // Start random glitch animations
            setInterval(animateGlitches, 2000);
        }, 500);
    }
})();
