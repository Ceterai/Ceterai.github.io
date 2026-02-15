// Random Alta Quote Generator
(function() {
    'use strict';
    
    let altaNames = [];
    let altaPhrases = [];
    
    // Fetch Alta names from GitHub
    async function fetchAltaNames() {
        try {
            const response = await fetch('https://raw.githubusercontent.com/Ceterai/Enternia/main/species/alta_namegen.config');
            const text = await response.text();
            
            // Strip comments and parse as JSON
            const jsonText = text.replace(/\/\/.*$/gm, '');
            const data = JSON.parse(jsonText);
            altaNames = data.names[1]; // Second element is the array of names
        } catch (e) {
            console.warn('Could not load Alta names:', e);
            altaNames = ['Nana', 'Mia', 'Ina', 'Remi'];
        }
    }
    
    // Fetch Alta dialog from GitHub
    async function fetchAltaPhrases() {
        try {
            const response = await fetch('https://raw.githubusercontent.com/Ceterai/Enternia/main/dialog/alta.config');
            const text = await response.text();
            
            // Strip comments and parse as JSON
            const jsonText = text.replace(/\/\/.*$/gm, '');
            const data = JSON.parse(jsonText);
            altaPhrases = data.converse.alta.generic;
        } catch (e) {
            console.warn('Could not load Alta phrases:', e);
            altaPhrases = [
                'The crystals sing to those who listen.',
                'Have you explored the depths of Enternia?',
                'I love all my alta sisters!',
                'How was your day, sweetheart?'
            ];
        }
    }
    
    // Generate random quote
    function generateQuote() {
        if (altaNames.length === 0 || altaPhrases.length === 0) {
            return { name: 'Alta', phrase: 'The crystals sing to those who listen.' };
        }
        
        const name = altaNames[Math.floor(Math.random() * altaNames.length)];
        const phrase = altaPhrases[Math.floor(Math.random() * altaPhrases.length)];
        
        return { name, phrase };
    }
    
    // Replace <!-- alta quote --> placeholder
    function replaceQuotePlaceholder(quote) {
        const placeholder = document.body.innerHTML;
        if (placeholder.includes('<!-- alta quote -->')) {
            const quoteHTML = `
                <div class="alta-quote-box">
                    <div class="quote-content">
                        <div class="quote-icon">💬</div>
                        <div class="quote-body">
                            <div class="quote-text">"${quote.phrase}"</div>
                            <div class="quote-author">— ${quote.name}</div>
                        </div>
                        <button class="quote-refresh" title="New quote" onclick="window.refreshAltaQuote()">⟳</button>
                    </div>
                </div>
            `;
            document.body.innerHTML = placeholder.replace('<!-- alta quote -->', quoteHTML);
        }
    }
    
    // Refresh quote function
    window.refreshAltaQuote = function() {
        const quote = generateQuote();
        const quoteText = document.querySelector('.alta-quote-box .quote-text');
        const quoteAuthor = document.querySelector('.alta-quote-box .quote-author');
        if (quoteText && quoteAuthor) {
            quoteText.textContent = `"${quote.phrase}"`;
            quoteAuthor.textContent = `— ${quote.name}`;
        }
    };
    
    // Initialize
    async function init() {
        // Check if placeholder exists
        if (!document.body.innerHTML.includes('<!-- alta quote -->')) return;
        
        await Promise.all([fetchAltaNames(), fetchAltaPhrases()]);
        
        const quote = generateQuote();
        replaceQuotePlaceholder(quote);
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
