# My Enternia Wiki Assets

## JavaScript Architecture

### Core Utilities

#### `utils.js` (MUST LOAD FIRST)
Shared utility library providing common functions used across all scripts:
- **DOM utilities**: `onDOMReady()`, `findCommentNode()`, `replaceComment()`
- **LocalStorage helpers**: `getFromStorage()`, `saveToStorage()`
- **Path utilities**: `isWikiPage()`, `pathIncludes()`
- **UI feedback**: `showNotification()`

**Global API**: `window.MyEnterniaUtils`

---

### Wiki Features

#### `bookmarks.js`
Bookmark/favorites system for wiki pages.
- Star button to bookmark current page
- Dropdown menu to view and manage bookmarks
- Search button for wiki
- Persistent storage using localStorage

**Dependencies**: `utils.js`

#### `stats-display.js`
Visual statistics display in wiki toolbar.
- View counter badge showing page visits
- Stats dropdown with detailed exploration data
- Integrates with bookmarks, view-counter, and secrets

**Dependencies**: `utils.js`, `view-counter.js`  
**Global API**: `window.myEnterniaStatsDisplay.updateSecretCount()`

#### `view-counter.js`
Backend tracking system for user exploration statistics.
- Tracks page visits per URL
- Counts links clicked, random pages used
- Provides data to stats-display

**Dependencies**: `utils.js`  
**Global API**: `window.myEnterniaStats`

#### `random-page.js`
Random wiki page navigation.
- Button in toolbar (🎲)
- Keyboard shortcut: Press `R` key
- Fetches pages from sitemap.xml → Pagefind → DOM

**Dependencies**: `utils.js`

---

### Content Enhancement

#### `alta-quotes.js`
Generates random Alta NPC quotes.
- Replaces `<!-- alta quote -->` HTML comments
- Fetches names and dialog from GitHub repository
- Refresh button to get new quote

**Dependencies**: `utils.js`

#### `alta-facts.js`
Displays random fun facts about the mod.
- Replaces `<!-- alta fact -->` HTML comments
- Curated list of interesting trivia
- Categorized by topic (Characters, Items, Biomes, etc.)

**Dependencies**: `utils.js`

#### `particles.js`
Visual particle effects for special pages.
- Automatic detection based on page content
- Snowflakes, hearts, stars, etc.

**Dependencies**: None

---

### Interactive Features

#### `secrets.js`
Hidden easter eggs and secret discoveries.
- **Type codes**: `uwu` (text transformer), `trail` (cursor effect)
- **Mystery boxes**: 1% spawn chance on wiki pages
- **Secret pages**: Special character pages grant achievements

**Dependencies**: `utils.js`  
**Global API**: `window.myEnterniaSecrets`

#### `copy-code.js`
One-click code copying for code blocks.
- Adds copy button to code blocks and inline code
- Visual feedback on copy success/failure
- Auto-reinitializes on dynamic content

**Dependencies**: `utils.js`

#### `text-glitch.js`
Cyberpunk-style text glitch effects.
- Applies to `.glitch` elements
- Animated character randomization

**Dependencies**: None

---

### UI Enhancements

#### `back-to-top.js`
Floating "back to top" button on scroll.
- Appears after scrolling down
- Smooth scroll animation
- Auto-hides on page top

**Dependencies**: `utils.js`

#### `support-button.js`
Support/donation floating badge.
- Appears on scroll
- Links to Buy Me a Coffee and Ko-fi
- Also adds to stats dropdown

**Dependencies**: `utils.js`

#### `console-messages.js`
Fun console messages for curious users.
- Generates unique UUID based on page
- Shows lucky number
- Easter egg for developers who check console

**Dependencies**: None

---

### Disabled Features

#### `idle-companion.js` (commented out in layout)
Idle detection easter egg.

#### `mood-system.js` (commented out in layout)
Page mood detection system.

---

## Load Order

Scripts load in this order (see `_layouts/default.html`):

1. **utils.js** ← MUST be first
2. bookmarks.js
3. view-counter.js ← Required by stats-display.js
4. stats-display.js
5. secrets.js
6. console-messages.js
7. particles.js
8. alta-quotes.js
9. alta-facts.js
10. support-button.js
11. back-to-top.js
12. random-page.js
13. copy-code.js
14. text-glitch.js

---

## localStorage Keys

- `myEnterniaBookmarks` - Bookmarked pages
- `myEnterniaPersonalViews` - Page view tracking
- `myEnterniaExtraStats` - Link clicks, random uses
- `myEnterniaSecretsFound` - Discovered easter eggs

---

## Global APIs

### `window.MyEnterniaUtils`
Core utilities (see utils.js)

### `window.myEnterniaStats`
```js
{
  trackLinkClick()
  trackRandomPage()
  getPersonalStats()
  checkFirstView(url)
  getCurrentPageViewCount()
  resetStats()
}
```

### `window.myEnterniaStatsDisplay`
```js
{
  updateSecretCount()
}
```

### `window.myEnterniaSecrets`
```js
{
  discover(secretId)
  isFound(secretId)
  getFoundCount()
  getTotalCount()
  reset()
}
```

### `window.refreshAltaQuote()`
Refresh the Alta quote on current page.

### `window.refreshAltaFact()`
Refresh the Alta fact on current page.

---

## Development Guidelines

### Adding New Scripts

1. Add IIFE wrapper: `(function() { 'use strict'; ... })();`
2. Add dependencies comment in header
3. Use `window.MyEnterniaUtils.onDOMReady()` for initialization
4. Use utility functions from `utils.js` when possible
5. Add to `_layouts/default.html` in appropriate order
6. Update this README

### LocalStorage Best Practices

```js
// ✅ Good - uses utils
const data = window.MyEnterniaUtils.getFromStorage('myKey', []);
window.MyEnterniaUtils.saveToStorage('myKey', data);

// ❌ Bad - manual error handling
try {
  const data = JSON.parse(localStorage.getItem('myKey') || '[]');
} catch(e) { ... }
```

### Path Checking Best Practices

```js
// ✅ Good - handles trailing slashes
if (window.MyEnterniaUtils.isWikiPage()) { ... }

// ❌ Bad - misses /MyEnternia/Wiki (no trailing slash)
if (window.location.pathname.includes('/MyEnternia/Wiki/')) { ... }
```

---

## Maintenance Notes

- All Wiki-specific features check `isWikiPage()` before initializing
- Notification systems use consistent patterns
- Event listeners are properly cleaned up
- Scripts are defensive against missing dependencies
