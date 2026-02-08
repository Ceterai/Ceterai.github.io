---
layout: default
title: "???"
---

<style>
.secret-page-gif {
    position: fixed;
    width: 44px;
    height: 44px;
    pointer-events: none;
    z-index: 100;
    animation: drift 20s infinite linear;
}

@keyframes drift {
    0% { transform: translate(0, 0) rotate(0deg); }
    25% { transform: translate(10vw, 10vh) rotate(90deg); }
    50% { transform: translate(-5vw, 20vh) rotate(180deg); }
    75% { transform: translate(15vw, -10vh) rotate(270deg); }
    100% { transform: translate(0, 0) rotate(360deg); }
}
</style>

<h1 style="text-align: center; color: var(--ct_7); animation: pulse 2s infinite;">Hey there~</h1>

<p style="text-align: center; font-size: 1.5rem;">
🎉 Welcome to the party! 🎉
</p>

<p style="text-align: center;">
Enjoy your stay, but don't look directly into the eyes!
</p>

<script>
// Spawn random floating gifs
for (let i = 0; i < 15; i++) {
    const gif = document.createElement('img');
    gif.src = '/art/ceterai_44.gif';
    gif.className = 'secret-page-gif';
    gif.style.left = Math.random() * 90 + '%';
    gif.style.top = Math.random() * 90 + '%';
    gif.style.animationDelay = Math.random() * 20 + 's';
    gif.style.animationDuration = (15 + Math.random() * 10) + 's';
    document.body.appendChild(gif);
}
</script>
