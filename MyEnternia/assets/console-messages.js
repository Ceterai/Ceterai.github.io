// Console Messages
(function() {
    'use strict';
    
    // Simple hash function for consistent encoding
    function hashString(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
            const char = str.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash;
        }
        return Math.abs(hash);
    }
    
    // Generate UUID7-like string from page title
    function generateUUID7Like(title) {
        const hash = hashString(title);
        const hex = hash.toString(16).padStart(32, '0');
        
        // Format as UUID7-like: xxxxxxxx-xxxx-7xxx-xxxx-xxxxxxxxxxxx
        return `${hex.slice(0,8)}-${hex.slice(8,12)}-7${hex.slice(13,16)}-${hex.slice(16,20)}-${hex.slice(20,32)}`;
    }
    
    // Convert UUID to 1-2 digit lucky number
    function getLuckyNumber(uuid) {
        const nums = uuid.replace(/-/g, '').match(/\d/g) || [];
        const sum = nums.reduce((acc, n) => acc + parseInt(n), 0);
        return (sum % 99) + 1; // 1-99
    }
    
    // Display console message
    function showConsoleMessage() {
        const title = document.title.split(' | ')[0].trim();
        const uuid = generateUUID7Like(title);
        const luckyNumber = getLuckyNumber(uuid);
        
        console.log('%c🌌 My Enternia Wiki 🌌', 'font-size: 20px; font-weight: bold; color: #64b5f6;');
        console.log(`%cYour guess is: ${uuid} 💙`, 'font-size: 14px; color: #90caf9;');
        console.log(`%cYour lucky number: ${luckyNumber}!`, 'font-size: 14px; color: #81c784; font-weight: bold;');
    }
    
    if (window.location.pathname.includes('/MyEnternia/')) {
        showConsoleMessage();
    }
})();
