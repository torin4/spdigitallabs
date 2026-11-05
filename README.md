# SP Digital Labs

Website for SP Digital Labs, the name under which Joseph Suzuki Parker publishes apps. Live at https://spdigitallabs.app (GitHub Pages, custom domain set in `CNAME`).

Plain static HTML, no build step. Preview locally with `python3 -m http.server` and open http://localhost:8000.

## Layout

- `index.html` - studio home and app list
- `style.css`, `email.js` - shared by every page (`email.js` builds the contact address in the browser so it isn't in the page source). Colors, type and spacing follow the SP Digital Labs design system.
- `fonts/` - self-hosted M PLUS Rounded 1c (headings) and IBM Plex Mono (labels)
- `assets/` - the SP logo tile and app icon; `apple-touch-icon.png` is the iPhone home-screen icon
- `dailyallowance/` - Daily Allowance home, privacy policy, terms, support and account deletion pages
- `404.html` - not-found page

To add an app, add a card to the list in `index.html` and, once it needs legal pages, a folder like `dailyallowance/`.
