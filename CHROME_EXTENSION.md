# Chrome New Tab Extension Installation

This guide explains how to install the Open Author Clock as a Chrome new tab extension.

## Features

- **Integrated Search Bar**: Search the web directly from your new tab page
- **Multiple Search Engines**: Choose from DuckDuckGo (default), Google, Bing, Brave, or Startpage
- **Literary Clock**: View time-relevant literary quotes throughout the day
- **Keyboard Shortcut**: Press `/` to focus the search bar instantly

## Installation Steps

1. **Download or Clone the Repository**
   ```bash
   git clone https://github.com/ambercaravalho/open-author-clock.git
   ```

2. **Open Chrome Extensions Page**
   - Navigate to `chrome://extensions/` in your Chrome browser
   - Or click the three-dot menu → More Tools → Extensions

3. **Enable Developer Mode**
   - Toggle the "Developer mode" switch in the top right corner

4. **Load the Extension**
   - Click "Load unpacked"
   - Select the `open-author-clock` folder
   - The extension should now appear in your extensions list

5. **Verify Installation**
   - Open a new tab in Chrome
   - You should see the literary clock with a search bar at the top

## Using the Extension

### Search Functionality
- Type your search query in the search bar
- Select your preferred search engine from the dropdown (defaults to DuckDuckGo)
- Press Enter or click the search button
- Your search engine preference is automatically saved

### Keyboard Shortcuts
- Press `/` to quickly focus the search bar from anywhere on the page

### Literary Clock
- The quote updates automatically every minute
- Time references in quotes are highlighted in bold
- The clock adjusts font size based on quote length

## Customization

You can customize the clock's behavior by editing `config.js`:

- **Update interval**: How often quotes refresh
- **Fade durations**: Transition speed for quote changes
- **Font sizes**: Adjust text sizing
- **Wake lock**: Keep screen awake while viewing

## Troubleshooting

**Search bar not appearing?**
- Clear your browser cache and reload the extension
- Check that all files are present in the extension directory

**Quotes not loading?**
- Ensure `data.json` is in the same directory as `index.html`
- Check the browser console for error messages

**Search engine preference not saving?**
- Grant the extension storage permissions in Chrome settings
- Try selecting a different search engine and then switching back

## Uninstalling

1. Go to `chrome://extensions/`
2. Find "Open Author Clock" in the list
3. Click "Remove"

## Privacy

This extension:
- Stores your search engine preference locally
- Does not collect or transmit any personal data
- Does not track your searches
- Works completely offline (except when performing searches)

## Support

For issues or questions, visit: https://github.com/ambercaravalho/open-author-clock/issues
