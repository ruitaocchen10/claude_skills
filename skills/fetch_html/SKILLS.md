---
name: fetch_html
description: Fetch a webpage's raw HTML to use as context for writing a scraper. Tries requests, httpx, and curl with browser-like headers to work around common 403 blocks. Use when a user wants to scrape a site and needs the actual HTML structure first.
---

# Fetch HTML

Fetch the raw HTML of a public webpage so it can be used as context for writing a scraper.

## When to Use

Use this skill when the user:

- Wants to write a scraper or crawler and needs to inspect the target page's HTML first
- Asks you to identify CSS selectors, element IDs, class names, or data patterns on a specific URL
- Gets 403 errors when trying to fetch a page

Do **not** use this skill for:

- Pages behind a login wall or paywall
- Pages that require user interaction to load content (e.g. clicking a "Load More" button with no direct URL)

## Steps

1. **Confirm the URL.** If the user hasn't provided one, ask for it before proceeding.

2. **Tell the user what you're doing.** Say something like:

   > "Fetching `<URL>` — trying requests → httpx → curl with browser-like headers..."

3. **Run the fetch script:**

   ```bash
   python3 ~/.claude/commands/fetch_html_scripts/fetch_html.py "<URL>"
   ```

   Capture stdout (HTML) and stderr (error messages). Note the exit code.

4. **On success (exit 0):**
   - Load the full HTML into context.
   - Briefly summarize the page structure: main containers, repeating patterns, data-bearing tags (tables, lists, article blocks, `data-*` attributes).
   - Identify the key CSS selectors or XPath patterns the user's scraper will need.
   - Proceed to write the scraper based on the actual HTML.

5. **On failure (exit 1):**
   - Tell the user clearly:
     > "All three strategies failed for `<URL>`. The site uses advanced bot-protection (Cloudflare, CAPTCHA, or JavaScript fingerprinting) that requires a real browser — this skill deliberately does not attempt to bypass those systems."
   - Offer alternatives:
     - Open the page in a browser → right-click → "Save As" or copy the page source → paste it here
     - Check if the site has an official API or sitemap
     - If they paste the HTML directly, proceed with writing the scraper from that

## Ethical Constraints

- Only fetch publicly accessible pages — no authentication, no paywalls.
- Do not retry on failure. One attempt per strategy is sufficient and respectful of the server.
- If all three strategies fail, stop. Do not look for additional bypass techniques.

## Using the Fetched HTML

Once you have the HTML:

1. **Identify the data containers** — find the outermost element that wraps the repeating data (e.g. `<ul id="results">`, `<table class="listings">`, `<div class="product-grid">`).

2. **Find the selector pattern** — look for stable identifiers: IDs, semantic class names, `data-*` attributes. Avoid positional selectors like `div:nth-child(3)` which break on layout changes.

3. **Check for pagination** — look for `<a rel="next">`, `?page=` URL parameters, or API calls in `<script>` tags that load more data.

4. **Note JavaScript-rendered content** — if the HTML shows a loading spinner or empty containers where you'd expect data, the content is rendered client-side. Mention this to the user — they'll need Playwright or Selenium for those cases.

5. **Write the scraper** using `requests` + `BeautifulSoup` for static pages, or note if a headless browser would be required.

## How the Script Works

The script at `~/.claude/commands/fetch_html_scripts/fetch_html.py` tries three strategies:

| Strategy | Library          | TLS Fingerprint       | Handles Brotli       |
| -------- | ---------------- | --------------------- | -------------------- |
| 1        | `requests`       | urllib3 / OpenSSL     | No (uses gzip only)  |
| 2        | `httpx` + HTTP/2 | ALPN `h2`             | Yes                  |
| 3        | `curl`           | macOS SecureTransport | Yes (`--compressed`) |

Each uses Chrome 124 browser-like headers including `Sec-Fetch-*` signals. Most 403s from public sites are caused by a missing or bot-like User-Agent — strategy 1 resolves these. Sites that check the TLS fingerprint are handled by strategies 2 and 3.

If all three fail, the site is using active bot-detection that requires a real browser session.
