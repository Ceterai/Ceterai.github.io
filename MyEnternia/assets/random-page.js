// Random Page Button for Wiki
(function() {
    'use strict';
    
    let allPages = [];
    let loadAttempted = false;
    
    // Fallback: Generate wiki page list from current page links
    function extractWikiPagesFromDOM() {
        const links = document.querySelectorAll('a[href*="/MyEnternia/Wiki/"]');
        const pages = new Set();
        
        links.forEach(link => {
            const href = link.getAttribute('href');
            if (href && href.includes('/MyEnternia/Wiki/') && !href.endsWith('/Wiki/')) {
                // Extract pathname
                try {
                    const url = new URL(href, window.location.origin);
                    pages.add(url.pathname);
                } catch (e) {
                    // If relative URL, just use it
                    if (href.startsWith('/')) {
                        pages.add(href);
                    }
                }
            }
        });
        
        return Array.from(pages);
    }
    
    // Fetch pages from sitemap
    async function fetchPagesFromSitemap() {
        try {
            const response = await fetch('/MyEnternia/sitemap.xml');
            if (!response.ok) throw new Error('Sitemap not found');
            
            const text = await response.text();
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(text, 'text/xml');
            const urls = Array.from(xmlDoc.getElementsByTagName('loc'));
            
            return urls
                .map(loc => {
                    const url = loc.textContent;
                    try {
                        const path = new URL(url).pathname;
                        return path;
                    } catch (e) {
                        return null;
                    }
                })
                .filter(path => path && path.includes('/MyEnternia/Wiki/') && !path.endsWith('/Wiki/'));
        } catch (e) {
            console.error('Error fetching sitemap:', e);
            return [];
        }
    }
    
    // Fetch pages from Pagefind index
    async function fetchFromPagefind() {
        try {
            if (typeof PagefindUI === 'undefined') return [];
            
            // Wait a bit for Pagefind to initialize
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            if (window.pagefind) {
                const search = await window.pagefind.search('');
                return search.results.map(r => r.url).filter(url => 
                    url && url.includes('/MyEnternia/Wiki/')
                );
            }
        } catch (e) {
            console.error('Error with Pagefind:', e);
        }
        return [];
    }
    
    // Fetch wiki pages using multiple strategies
    async function fetchWikiPages() {
        if (loadAttempted) return;
        loadAttempted = true;
        
        try {
            // Strategy 1: Try sitemap first (most reliable)
            let pages = await fetchPagesFromSitemap();
            
            // Strategy 2: If sitemap fails, try Pagefind
            if (pages.length === 0) {
                pages = await fetchFromPagefind();
            }
            
            // Strategy 3: Extract from current page as last resort
            if (pages.length === 0) {
                pages = extractWikiPagesFromDOM();
            }
            
            allPages = pages;
            console.log(`Loaded ${allPages.length} wiki pages for random navigation`);
        } catch (e) {
            console.error('Error fetching wiki pages:', e);
            // Try DOM extraction as final fallback
            allPages = extractWikiPagesFromDOM();
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
    async function goToRandomPage() {
        // If pages not loaded yet, try loading them now
        if (allPages.length === 0 && !loadAttempted) {
            const button = document.getElementById('random-page-button');
            if (button) {
                button.innerHTML = '⏳';
                button.disabled = true;
            }
            
            await fetchWikiPages();
            
            if (button) {
                button.innerHTML = '🎲';
                button.disabled = false;
            }
        }
        
        const randomPage = getRandomPage();
        if (randomPage) {
            // Track random page usage
            if (window.myEnterniaStats) {
                window.myEnterniaStats.trackRandomPage();
            }
            
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
            alert('Could not find wiki pages. Try navigating to another wiki page first, then try again.');
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
        // Only initialize on Wiki pages
        const isWikiPage = (window.location.pathname + '/').includes('/MyEnternia/Wiki/');
        
        if (!isWikiPage) {
            return;
        }
        
        // Create random button
        const randomButton = document.createElement('button');
        randomButton.id = 'random-page-button';
        randomButton.className = 'wiki-tool-btn';
        randomButton.innerHTML = '🎲';
        randomButton.title = 'Go to random wiki page (Press R)';
        randomButton.addEventListener('click', goToRandomPage);
        
        // Insert into the wiki-tools bar
        const toolsBar = document.getElementById('wiki-tools');
        if (toolsBar) {
            toolsBar.appendChild(randomButton);
        }
        
        // Setup keyboard shortcut
        setupKeyboardShortcut();
        
        // Start loading pages in background (don't wait)
        fetchWikiPages();
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initRandomPageButton);
    } else {
        initRandomPageButton();
    }
})();
