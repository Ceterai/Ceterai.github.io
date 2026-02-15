// Page Mood System - Visual overlays and effects based on page content
(function() {
    'use strict';
    
    const moods = {
        love: {
            color: 'rgba(252, 176, 224, 0.08)', // Soft pink
            gradient: 'linear-gradient(135deg, rgba(252, 96, 192, 0.1) 0%, rgba(252, 176, 224, 0.05) 100%)',
            glow: 'rgba(252, 176, 224, 0.3)',
            keywords: ['estria', 'miko', 'yae', 'ava', 'sunset', 'companion', 'girlfriend', 'love', 'estra']
        },
        void: {
            color: 'rgba(20, 20, 30, 0.15)', // Dark depressing
            gradient: 'linear-gradient(135deg, rgba(10, 10, 15, 0.2) 0%, rgba(30, 20, 40, 0.1) 100%)',
            glow: 'rgba(80, 60, 100, 0.4)',
            keywords: ['void', 'abyss', 'empty', 'darkness', 'alone']
        },
        corrupted: {
            color: 'rgba(0, 150, 200, 0.08)', // Sad blue/cyan
            gradient: 'linear-gradient(135deg, rgba(0, 100, 150, 0.12) 0%, rgba(100, 150, 200, 0.06) 100%)',
            glow: 'rgba(0, 200, 255, 0.4)',
            keywords: ['c.t.', 'ct_', 'corrupted', 'glitch', 'error']
        },
        mysterious: {
            color: 'rgba(120, 80, 180, 0.08)', // Purple mystical
            gradient: 'linear-gradient(135deg, rgba(120, 80, 180, 0.1) 0%, rgba(80, 40, 120, 0.05) 100%)',
            glow: 'rgba(150, 100, 200, 0.3)',
            keywords: ['ancient', 'mysterious', 'miazma', 'arcane', 'secret', 'hidden', 'enchanted']
        },
        nature: {
            color: 'rgba(80, 200, 120, 0.08)', // Fresh green
            gradient: 'linear-gradient(135deg, rgba(80, 200, 120, 0.1) 0%, rgba(120, 220, 150, 0.05) 100%)',
            glow: 'rgba(100, 220, 140, 0.3)',
            keywords: ['garden', 'forest', 'nature', 'plant', 'flora', 'tree', 'flower', 'bush', 'grass', 'grove', 'forest']
        }
    };
    
    function detectMood() {
        // Only check the h1 header
        const h1 = document.querySelector('h1');
        if (!h1) return null;
        
        const h1Text = h1.innerText.toLowerCase();
        
        // Check each mood
        for (const [moodName, moodData] of Object.entries(moods)) {
            for (const keyword of moodData.keywords) {
                if (h1Text.includes(keyword.toLowerCase())) {
                    return { name: moodName, data: moodData };
                }
            }
        }
        
        return null;
    }
    
    function applyMood(mood) {
        // Create overlay element
        const overlay = document.createElement('div');
        overlay.className = 'mood-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            z-index: 1;
            background: ${mood.data.gradient};
            opacity: 0;
            transition: opacity 1s ease-in;
        `;
        
        document.body.appendChild(overlay);
        
        // Fade in
        setTimeout(() => {
            overlay.style.opacity = '1';
        }, 100);
        
        // Add subtle pulse animation
        const style = document.createElement('style');
        style.textContent = `
            .mood-overlay {
                animation: mood-pulse 8s ease-in-out infinite;
            }
            
            @keyframes mood-pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
            
            /* Enhance links with mood color */
            body a:hover {
                text-shadow: 0 0 8px ${mood.data.glow};
            }
            
            /* Add subtle border glow to main content */
            main, article {
                box-shadow: inset 0 0 30px ${mood.data.color};
            }
        `;
        document.head.appendChild(style);
        
        // Console message
        console.log(`%c✨ Mood detected: ${mood.name}`, `color: ${mood.data.glow}; font-size: 12px;`);
    }
    
    // Initialize on wiki pages
    if (window.location.pathname.includes('/MyEnternia/')) {
        setTimeout(() => {
            const mood = detectMood();
            if (mood) {
                applyMood(mood);
            }
        }, 500);
    }
})();
