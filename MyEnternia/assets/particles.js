// Particle Effects for Special Pages
(function() {
    'use strict';
    
    function createParticle(type) {
        const particle = document.createElement('div');
        particle.className = `particle particle-${type}`;
        
        // Random starting position
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDuration = (3 + Math.random() * 4) + 's';
        particle.style.animationDelay = Math.random() * 5 + 's';
        
        if (type === 'snow') {
            particle.innerHTML = ['❅', '❆'][Math.floor(Math.random() * 2)];
            // Random blue/cyan shades for snow
            const snowColors = ['#cce8ff', '#b0e0fc', '#a0d8fc', '#d0f0ff'];
            particle.style.color = snowColors[Math.floor(Math.random() * snowColors.length)];
        } else if (type === 'stars') {
            particle.innerHTML = ['★'][Math.floor(Math.random() * 1)];
            // Random colors: green, blue, purple
            const starColors = ['#20f080', '#2080f0', '#8020f0'];
            particle.style.color = starColors[Math.floor(Math.random() * starColors.length)];
            particle.style.filter = `drop-shadow(0 0 5px ${particle.style.color})`;
        }
        
        document.body.appendChild(particle);
        
        // Remove after animation
        setTimeout(() => particle.remove(), 8000);
    }
    
    function startParticleEffect(type, count = 20) {
        // Create initial particles
        for (let i = 0; i < count; i++) {
            setTimeout(() => createParticle(type), i * 300);
        }
        
        // Keep creating new particles
        setInterval(() => createParticle(type), 500);
    }
    
    // Check page URL for keywords
    function checkForParticles() {
        const path = window.location.pathname.toLowerCase();
        
        if (path.includes('sona') || path.includes('sonaveil')) {
            startParticleEffect('snow');
        } else if (path.includes('stardust')) {
            startParticleEffect('stars');
        }
    }
    
    if (window.location.pathname.includes('/MyEnternia/Wiki/')) {
        checkForParticles();
    }
})();
