# BrainMap Demo

An interactive 2D brain map. Type a life situation and the brain regions involved light up, from blue (slightly involved) to pink (very involved), with a table explaining each region's role.

- Single static page (`index.html`): no build step, no backend.
- 50 preset situations are matched in the browser with per-situation rules.
- Anything else is sent to Claude using your own API key, which is stored only in your browser. Answers are cached locally.

Brain drawings will be adapted from Wikimedia Commons (CC BY-SA); credits will be listed here and on the page.
