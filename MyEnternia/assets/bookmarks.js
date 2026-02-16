/**
 * Bookmark/Favorites System for Wiki Pages
 * 
 * Features:
 * - Add/remove bookmarks with star button
 * - View and manage bookmarks in dropdown menu
 * - Persistent storage using localStorage
 * - Search button for wiki
 * 
 * Dependencies: utils.js
 */
(function() {
    'use strict';
    
    const STORAGE_KEY = 'myEnterniaBookmarks';
    
    // Get all bookmarks from localStorage
    const getBookmarks = () => window.MyEnterniaUtils.getFromStorage(STORAGE_KEY, []);
    
    // Save bookmarks to localStorage
    const saveBookmarks = (bookmarks) => window.MyEnterniaUtils.saveToStorage(STORAGE_KEY, bookmarks);
    
    // Check if current page is bookmarked
    function isBookmarked(url) {
        const bookmarks = getBookmarks();
        return bookmarks.some(b => b.url === url);
    }
    
    // Add bookmark
    function addBookmark(url, title) {
        const bookmarks = getBookmarks();
        if (!isBookmarked(url)) {
            bookmarks.push({
                url: url,
                title: title,
                timestamp: Date.now()
            });
            saveBookmarks(bookmarks);
            return true;
        }
        return false;
    }
    
    // Remove bookmark
    function removeBookmark(url) {
        let bookmarks = getBookmarks();
        bookmarks = bookmarks.filter(b => b.url !== url);
        saveBookmarks(bookmarks);
    }
    
    // Toggle bookmark
    function toggleBookmark() {
        const url = window.location.pathname;
        // Get title from h1 element, fallback to document.title
        const h1 = document.querySelector('h1');
        const title = h1 ? h1.textContent.trim() : document.title.split(' | ')[0].trim();
        
        if (isBookmarked(url)) {
            removeBookmark(url);
            updateBookmarkButton(false);
            showNotification('Removed from bookmarks');
        } else {
            addBookmark(url, title);
            updateBookmarkButton(true);
            showNotification('Added to bookmarks');
        }
        
        updateBookmarksList();
    }
    
    // Update bookmark button state
    function updateBookmarkButton(bookmarked) {
        const button = document.getElementById('bookmark-button');
        if (button) {
            button.classList.toggle('bookmarked', bookmarked);
            button.innerHTML = bookmarked ? '★' : '☆';
            button.title = bookmarked ? 'Remove from bookmarks' : 'Add to bookmarks';
        }
    }
    
    // Show notification
    function showNotification(message) {
        window.MyEnterniaUtils.showNotification(message, 2000, 'bookmark-notification');
    }
    
    // Update bookmarks list in menu
    function updateBookmarksList() {
        const list = document.getElementById('bookmarks-list');
        if (!list) return;
        
        const bookmarks = getBookmarks();
        
        if (bookmarks.length === 0) {
            list.innerHTML = '<div class="empty-bookmarks">No bookmarks yet</div>';
            return;
        }
        
        // Sort by timestamp (newest first)
        bookmarks.sort((a, b) => b.timestamp - a.timestamp);
        
        list.innerHTML = bookmarks.map(bookmark => `
            <div class="bookmark-item">
                <a href="${bookmark.url}" class="bookmark-link">${bookmark.title}</a>
                <button class="bookmark-remove" data-url="${bookmark.url}" title="Remove bookmark">×</button>
            </div>
        `).join('');
        
        // Add remove handlers
        list.querySelectorAll('.bookmark-remove').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const url = btn.dataset.url;
                removeBookmark(url);
                updateBookmarksList();
                if (window.location.pathname === url) {
                    updateBookmarkButton(false);
                }
                showNotification('Bookmark removed');
            });
        });
    }
    
    // Toggle bookmarks menu
    function toggleBookmarksMenu() {
        const menu = document.getElementById('bookmarks-menu');
        if (menu) {
            menu.classList.toggle('show');
        }
    }
    
    // Initialize bookmark system
    function initBookmarkSystem() {
        // Only initialize on Wiki pages
        if (!window.MyEnterniaUtils.isWikiPage()) return;
        
        // Create bookmark buttons as a fragment
        const container = document.createDocumentFragment();
        
        const bookmarkBtn = document.createElement('button');
        bookmarkBtn.id = 'bookmark-button';
        bookmarkBtn.className = 'wiki-tool-btn';
        bookmarkBtn.title = 'Bookmark this page';
        bookmarkBtn.innerHTML = '☆';
        container.appendChild(bookmarkBtn);
        
        // Add search button
        const searchBtn = document.createElement('a');
        searchBtn.href = '/MyEnternia/search.html';
        searchBtn.className = 'wiki-tool-btn';
        searchBtn.title = 'Search wiki';
        searchBtn.innerHTML = '🔍';
        container.appendChild(searchBtn);
        
        const menuWrapper = document.createElement('div');
        menuWrapper.className = 'bookmarks-menu-wrapper';
        menuWrapper.innerHTML = `
            <button id="bookmarks-menu-button" class="wiki-tool-btn" title="View bookmarks">
                📚 <span>${getBookmarks().length}</span>
            </button>
            <div id="bookmarks-menu" class="bookmarks-menu">
                <div class="bookmarks-menu-header">
                    <h3>Bookmarked Pages</h3>
                    <button class="close-menu" title="Close">×</button>
                </div>
                <div id="bookmarks-list" class="bookmarks-list"></div>
            </div>
        `;
        container.appendChild(menuWrapper);
        
        // Insert into the wiki-tools bar in the breadcrumbs
        const toolsBar = document.getElementById('wiki-tools');
        if (toolsBar) {
            toolsBar.appendChild(container);
        }
        
        // Set initial button state
        const url = window.location.pathname;
        updateBookmarkButton(isBookmarked(url));
        updateBookmarksList();
        
        // Add event listeners
        document.getElementById('bookmark-button').addEventListener('click', toggleBookmark);
        
        const menuBtn = document.getElementById('bookmarks-menu-button');
        if (menuBtn) {
            menuBtn.addEventListener('click', toggleBookmarksMenu);
        }
        
        const closeBtn = menuWrapper.querySelector('.close-menu');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                const menu = document.getElementById('bookmarks-menu');
                if (menu) menu.classList.remove('show');
            });
        }
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            const menu = document.getElementById('bookmarks-menu');
            const menuBtn = document.getElementById('bookmarks-menu-button');
            if (menu && !menu.contains(e.target) && !menuBtn.contains(e.target)) {
                menu.classList.remove('show');
            }
        });
    }
    
    // Initialize when DOM is ready
    window.MyEnterniaUtils.onDOMReady(initBookmarkSystem);
})();
