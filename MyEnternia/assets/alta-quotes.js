/**
 * Random Alta Quote Generator
 * 
 * Dynamically generates random Alta quotes on pages with <!-- alta quote --> comment.
 * Fetches names and dialog phrases from GitHub repository.
 * 
 * Dependencies: utils.js
 */
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
            altaPhrases = altaPhrases.concat(
                data.dancer.alta.alta,
                data.dancer.alta.generic,
                data.official.alta.alta,
                data.science.alta.alta,
                data.science.alta.generic,
                data.social.alta.generic,
                data.merc.alta.generic,
                data.botanist.alta.generic,
                data.botanist.alta.alta,
            );
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
        const quoteBox = document.createElement('div');
        quoteBox.className = 'alta-quote-box';
        quoteBox.innerHTML = `
            <div class="quote-content">
                <div class="quote-icon">💬</div>
                <div class="quote-body">
                    <div class="quote-text">"${quote.phrase}"</div>
                    <div class="quote-author">— ${quote.name}</div>
                </div>
                <button class="quote-refresh" title="New quote">⟳</button>
            </div>
        `;
        
        // Attach event listener
        const refreshBtn = quoteBox.querySelector('.quote-refresh');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', window.refreshAltaQuote);
        }
        
        // Replace comment with element
        window.MyEnterniaUtils.replaceComment('alta quote', quoteBox);
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
        if (!window.MyEnterniaUtils.findCommentNode('alta quote')) return;
        
        await Promise.all([fetchAltaNames(), fetchAltaPhrases()]);
        
        const quote = generateQuote();
        replaceQuotePlaceholder(quote);
    }
    
    window.MyEnterniaUtils.onDOMReady(init);
})();
