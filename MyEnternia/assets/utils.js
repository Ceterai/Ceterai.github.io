/**
 * My Enternia Wiki Utilities
 * Shared helper functions used across multiple scripts
 */
(function() {
    'use strict';

    // =============================================================================
    // DOM Utilities
    // =============================================================================

    /**
     * Execute callback when DOM is ready
     * @param {Function} callback - Function to execute when DOM is ready
     */
    function onDOMReady(callback) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', callback);
        } else {
            callback();
        }
    }

    /**
     * Find HTML comment node by content
     * @param {string} commentText - Text content of the comment to find
     * @param {Node} root - Root node to search from (default: document.body)
     * @returns {Comment|null} - Found comment node or null
     */
    function findCommentNode(commentText, root = document.body) {
        const walker = document.createTreeWalker(
            root,
            NodeFilter.SHOW_COMMENT,
            null,
            false
        );
        
        while (walker.nextNode()) {
            if (walker.currentNode.nodeValue.trim() === commentText) {
                return walker.currentNode;
            }
        }
        return null;
    }

    /**
     * Replace HTML comment with an element
     * @param {string} commentText - Text content of the comment to find
     * @param {HTMLElement} newElement - Element to replace the comment with
     * @returns {boolean} - True if replacement was successful
     */
    function replaceComment(commentText, newElement) {
        const comment = findCommentNode(commentText);
        if (comment && comment.parentNode) {
            comment.parentNode.replaceChild(newElement, comment);
            return true;
        }
        return false;
    }

    // =============================================================================
    // LocalStorage Utilities
    // =============================================================================

    /**
     * Safely get JSON data from localStorage
     * @param {string} key - LocalStorage key
     * @param {*} defaultValue - Value to return if key doesn't exist or parsing fails
     * @returns {*} - Parsed value or default
     */
    function getFromStorage(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (e) {
            console.warn(`Error reading from localStorage (${key}):`, e);
            return defaultValue;
        }
    }

    /**
     * Safely save JSON data to localStorage
     * @param {string} key - LocalStorage key
     * @param {*} value - Value to save (will be JSON stringified)
     * @returns {boolean} - True if save was successful
     */
    function saveToStorage(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (e) {
            console.error(`Error saving to localStorage (${key}):`, e);
            return false;
        }
    }

    // =============================================================================
    // Path Utilities
    // =============================================================================

    /**
     * Check if current page is a Wiki page
     * Handles both /MyEnternia/Wiki and /MyEnternia/Wiki/ paths
     * @returns {boolean} - True if on a Wiki page
     */
    function isWikiPage() {
        return (window.location.pathname + '/').includes('/MyEnternia/Wiki/');
    }

    /**
     * Check if path matches a pattern (normalizes trailing slashes)
     * @param {string} pattern - Pattern to match
     * @returns {boolean} - True if current path matches pattern
     */
    function pathIncludes(pattern) {
        return (window.location.pathname + '/').includes(pattern);
    }

    // =============================================================================
    // UI Feedback Utilities
    // =============================================================================

    /**
     * Show a temporary notification toast
     * @param {string} message - Message to display
     * @param {number} duration - Duration in milliseconds (default: 2000)
     * @param {string} className - Additional CSS class name (optional)
     */
    function showNotification(message, duration = 2000, className = '') {
        const notification = document.createElement('div');
        notification.className = `temp-notification ${className}`.trim();
        notification.textContent = message;
        
        // Add basic inline styles if no stylesheet is loaded
        if (!className) {
            Object.assign(notification.style, {
                position: 'fixed',
                bottom: '20px',
                right: '20px',
                padding: '12px 24px',
                background: '#333',
                color: '#fff',
                borderRadius: '4px',
                boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
                zIndex: '10000',
                opacity: '0',
                transition: 'opacity 0.3s ease',
                fontSize: '14px'
            });
        }
        
        document.body.appendChild(notification);
        
        // Trigger animation
        requestAnimationFrame(() => {
            notification.style.opacity = '1';
        });
        
        // Remove after duration
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.remove();
                }
            }, 300);
        }, duration);
    }

    // =============================================================================
    // Export to global namespace
    // =============================================================================

    window.MyEnterniaUtils = {
        // DOM
        onDOMReady,
        findCommentNode,
        replaceComment,
        
        // Storage
        getFromStorage,
        saveToStorage,
        
        // Path
        isWikiPage,
        pathIncludes,
        
        // UI
        showNotification
    };

})();
