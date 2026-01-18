# Open Author Clock ⏰

An open-source, web-based implementation of the Author Clock Kickstarter project that runs as a Chrome new tab extension with integrated web search.

## ✨ Features ✨

- **Literary Clock**: Display time-relevant quotes from literature for every minute of the day
- **Integrated Search**: Search the web directly from your new tab page
- **Multiple Search Engines**: Choose from DuckDuckGo (default), Google, Bing, Brave, or Startpage
- **Keyboard Shortcuts**: Press `/` to instantly focus the search bar
- **Dark Mode**: Automatic dark mode support based on system preferences

## ✨ See It in Action ✨

Why confine the words of literature to pages of a book? This project brings literary quotes to every minute of your day, telling time through the words of authors from times gone by.

<p align="center">
<img src="example-photo.jpg" height="400">

Try it out for yourself: [__Live Demo Site 🖥️__](https://clock.ambercaravalho.com)

### Inspiration

This project was sparked by two main projects:

- [The Author Clock](https://www.authorclock.com): A dedicated gadget that tells time through literary quotes, offering a new hand-picked passage every minute.

- The [literaryclock repo](https://github.com/elegantalchemist/literaryclock) by [elegantalchemist](https://github.com/elegantalchemist): The idea of a literary clock already executed on the Kindle Keyboard using Python.

## Installation as Chrome Extension

To use this as your Chrome new tab page:

1. Clone or download this repository
2. Open Chrome and go to `chrome://extensions/`
3. Enable "Developer mode" in the top right
4. Click "Load unpacked" and select the project folder
5. Open a new tab to see the literary clock with search functionality

For detailed installation instructions, see [CHROME_EXTENSION.md](CHROME_EXTENSION.md).

## Configuration

You can customize the clock's behavior by editing `config.js`:

- **Update interval**: How often the quote updates
- **Fade durations**: Transition speed for quote changes
- **Font sizes**: Adjust text sizing for different quote lengths
- **Wake lock**: Keep screen awake while viewing
- **UTC timezone**: Automatic adjustment for UTC devices

## Contributing to the Quote List

If you've stumbled upon a quote that perfectly captures a minute, feel free to contribute!

### Quote Formatting

Each quote should be formatted as a JSON object in the `data.json` file:

```json
{
  "time": "14:45",
  "timeString": "quarter to three",
  "quote": "The full sentence from the book where the time is mentioned.",
  "title": "Book Title",
  "author": "Author Name"
}
```

- **time**: The specific time the quote represents, in 24-hour format (e.g., `14:45`).
- **timeString**: The way the time is mentioned within the quote, to be highlighted (e.g., `quarter to three`).
- **quote**: The full sentence from the book where the time is mentioned.
- **title**: The title of the book the quote is from.
- **author**: The author of the book.

For example:

```json
{
  "time": "00:00",
  "timeString": "midnight",
  "quote": "It starts at midnight.",
  "title": "Catching Fire",
  "author": "Suzanne Collins"
}
```

### Where to Add Your Quote

1. Open the `data.json` file
2. Find the appropriate time slot (quotes are ordered by time)
3. Add your new quote object to the array
4. Ensure proper JSON formatting (don't forget commas between objects!)

## More Info

### Known Issues

Visit this repo's [Issues](https://github.com/ambercaravalho/open-author-clock/issues) page to see known issues and contribute to make this project even better!

### License Disclaimer

This project uses quotes sourced from the [literaryclock](https://github.com/elegantalchemist/literaryclock) repo under the GNU General Public License v3.0.
