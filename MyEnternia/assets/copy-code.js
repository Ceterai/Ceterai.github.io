// Copy-to-Clipboard for Code Blocks
(function() {
    'use strict';
    
    // Copy text to clipboard
    async function copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            return true;
        } catch (err) {
            // Fallback for older browsers
            try {
                const textArea = document.createElement('textarea');
                textArea.value = text;
                textArea.style.position = 'fixed';
                textArea.style.left = '-999999px';
                document.body.appendChild(textArea);
                textArea.focus();
                textArea.select();
                const successful = document.execCommand('copy');
                document.body.removeChild(textArea);
                return successful;
            } catch (err2) {
                console.error('Failed to copy:', err2);
                return false;
            }
        }
    }
    
    // Show copy feedback
    function showCopyFeedback(button, success) {
        const originalHTML = button.innerHTML;
        
        if (success) {
            button.innerHTML = '✓ Copied!';
            button.classList.add('copied');
        } else {
            button.innerHTML = '✗ Failed';
            button.classList.add('failed');
        }
        
        setTimeout(() => {
            button.innerHTML = originalHTML;
            button.classList.remove('copied', 'failed');
        }, 2000);
    }
    
    // Create copy button
    function createCopyButton(codeBlock) {
        const button = document.createElement('button');
        button.className = 'copy-code-button';
        button.innerHTML = '📋 Copy';
        button.title = 'Copy to clipboard';
        
        button.addEventListener('click', async () => {
            const code = codeBlock.textContent;
            const success = await copyToClipboard(code);
            showCopyFeedback(button, success);
        });
        
        return button;
    }
    
    // Add copy buttons to code blocks
    function addCopyButtonsToCodeBlocks() {
        // Find all pre > code blocks (syntax highlighted code)
        const codeBlocks = document.querySelectorAll('pre > code');
        
        codeBlocks.forEach(codeBlock => {
            const pre = codeBlock.parentElement;
            
            // Skip if already has a copy button
            if (pre.querySelector('.copy-code-button')) {
                return;
            }
            
            // Wrap pre in a container for positioning
            const wrapper = document.createElement('div');
            wrapper.className = 'code-block-wrapper';
            pre.parentNode.insertBefore(wrapper, pre);
            wrapper.appendChild(pre);
            
            // Create and add copy button
            const copyButton = createCopyButton(codeBlock);
            wrapper.appendChild(copyButton);
        });
    }
    
    // Add copy button for inline code (on hover)
    function addCopyButtonsToInlineCode() {
        const inlineCodes = document.querySelectorAll('p > code, li > code, td > code');
        
        inlineCodes.forEach(code => {
            // Only add to longer code snippets (more than 10 characters)
            if (code.textContent.length < 10) {
                return;
            }
            
            code.classList.add('copyable-inline-code');
            code.title = 'Click to copy';
            
            code.addEventListener('click', async () => {
                const success = await copyToClipboard(code.textContent);
                
                // Show temporary feedback
                const originalContent = code.textContent;
                if (success) {
                    code.classList.add('copied');
                    setTimeout(() => {
                        code.classList.remove('copied');
                    }, 1000);
                }
            });
        });
    }
    
    // Initialize copy functionality
    function initCopyToClipboard() {
        // Only initialize on Wiki pages
        if (!window.location.pathname.includes('/MyEnternia/')) {
            return;
        }
        
        addCopyButtonsToCodeBlocks();
        addCopyButtonsToInlineCode();
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCopyToClipboard);
    } else {
        initCopyToClipboard();
    }
    
    // Re-initialize if content is dynamically added
    // (useful for single-page applications)
    const observer = new MutationObserver((mutations) => {
        let shouldReinit = false;
        
        mutations.forEach(mutation => {
            mutation.addedNodes.forEach(node => {
                if (node.nodeType === 1 && (node.tagName === 'PRE' || node.querySelector('pre'))) {
                    shouldReinit = true;
                }
            });
        });
        
        if (shouldReinit) {
            initCopyToClipboard();
        }
    });
    
    // Start observing
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
