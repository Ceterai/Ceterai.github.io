// Random Page Button for Wiki
(function() {
    'use strict';
    
    // Generate list of all wiki pages
    const wikiPages = [
        // This will be populated dynamically from the search index
    ];
    
    let allPages = [];
    
    // Fetch pages from Pagefind index
    async function fetchWikiPages() {
        try {
            // Try to get pages from Pagefind
            if (window.pagefind) {
                const search = await window.pagefind.search('');
                allPages = search.results.map(r => r.url).filter(url => 
                    url && url.includes('/MyEnternia/Wiki/')
                );
            } else {
                // Fallback: use a predefined list if Pagefind isn't available
                // In production, you might want to generate this list at build time
                allPages = await fetchPagesFromSitemap();
            }
        } catch (e) {
            console.error('Error fetching wiki pages:', e);
            allPages = [];
        }
    }
    
    // Fallback: fetch from sitemap
    async function fetchPagesFromSitemap() {
        try {
            const response = await fetch('/MyEnternia/sitemap.xml');
            const text = await response.text();
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(text, 'text/xml');
            const urls = Array.from(xmlDoc.getElementsByTagName('loc'));
            return urls
                .map(loc => {
                    const url = loc.textContent;
                    const path = new URL(url).pathname;
                    return path;
                })
                .filter(path => path.includes('/MyEnternia/Wiki/') && !path.endsWith('/Wiki/'));
        } catch (e) {
            console.error('Error fetching sitemap:', e);
            return [];
        }
    }
    
    // Get random page URL
    function getRandomPage() {
        if (allPages.length === 0) {
            return null;
        }
        
        // Exclude current page
        const currentPath = window.location.pathname;
        const availablePages = allPages.filter(page => page !== currentPath);
        
        if (availablePages.length === 0) {
            return allPages[Math.floor(Math.random() * allPages.length)];
        }
        
        return availablePages[Math.floor(Math.random() * availablePages.length)];
    }
    
    // Navigate to random page
    function goToRandomPage() {
        const randomPage = getRandomPage();
        if (randomPage) {
            // Add animation
            const button = document.getElementById('random-page-button');
            if (button) {
                button.classList.add('spinning');
            }
            
            // Navigate after brief animation
            setTimeout(() => {
                window.location.href = randomPage;
            }, 500);
        } else {
            alert('Could not load wiki pages. Please try again.');
        }
    }
    
    // Add keyboard shortcut (R key)
    function setupKeyboardShortcut() {
        document.addEventListener('keydown', (e) => {
            // Only trigger if R is pressed (not in an input field)
            if (e.key === 'r' && !e.ctrlKey && !e.metaKey && !e.altKey && !e.shiftKey) {
                const activeElement = document.activeElement;
                const isInputField = activeElement.tagName === 'INPUT' || 
                                   activeElement.tagName === 'TEXTAREA' || 
                                   activeElement.isContentEditable;
                
                if (!isInputField) {
                    e.preventDefault();
                    goToRandomPage();
                }
            }
        });
    }
    
    // Initialize random page button
    async function initRandomPageButton() {
        // Only initialize on Wiki pages or search page
        const isWikiPage = window.location.pathname.includes('/MyEnternia/Wiki/');
        const isSearchPage = window.location.pathname.includes('/MyEnternia/search');
        
        if (!isWikiPage && !isSearchPage) {
            return;
        }
        
        // Fetch pages list
        await fetchWikiPages();
        
        // Create random button
        const randomButton = document.createElement('button');
        randomButton.id = 'random-page-button';
        randomButton.className = 'random-page-button';
        randomButton.innerHTML = '🎲 <span>Random Page</span>';
        randomButton.title = 'Go to random wiki page (Press R)';
        randomButton.addEventListener('click', goToRandomPage);
        
        // Find bookmark container or create one
        let container = document.querySelector('.bookmark-container');
        
        if (!container) {
            // If no bookmark container, create a button container
            container = document.createElement('div');
            container.className = 'wiki-tools-container';
            
            const h1 = document.querySelector('.ct_body h1');
            if (h1) {
                h1.after(container);
            } else {
                const body = document.querySelector('.ct_body');
                if (body) {
                    body.insertBefore(container, body.firstChild);
                }
            }
        }
        
        container.appendChild(randomButton);
        
        // Setup keyboard shortcut
        setupKeyboardShortcut();
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initRandomPageButton);
    } else {
        initRandomPageButton();
    }
})();
