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
            particle.innerHTML = ['❄️', '❅', '❆'][Math.floor(Math.random() * 3)];
        } else if (type === 'stars') {
            particle.innerHTML = ['⭐'][Math.floor(Math.random() * 1)];
        }
        
        document.body.appendChild(particle);
        
        // Remove after animation
        setTimeout(() => particle.remove(), 8000);
    }
    
    function startParticleEffect(type, count = 15) {
        // Create initial particles
        for (let i = 0; i < count; i++) {
            setTimeout(() => createParticle(type), i * 300);
        }
        
        // Keep creating new particles
        setInterval(() => createParticle(type), 2000);
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
