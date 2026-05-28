#!/usr/bin/env python3
"""
fetch_html.py — Fetch a webpage's HTML with browser-like headers.
Tries three strategies in order to work around common bot-detection.

Usage: python3 fetch_html.py <URL>
  stdout: raw HTML on success
  stderr: progress/error messages
  exit 0: success, exit 1: all strategies failed
"""

import sys
import subprocess

# Chrome 124 on macOS headers. Used by all three strategies.
# Note: Accept-Encoding intentionally excludes 'br' (Brotli) for the requests
# strategy because requests cannot decode Brotli natively — sending 'br' and
# getting a Brotli response would produce garbled output. httpx and curl handle
# Brotli fine and use the full Accept-Encoding via their own mechanisms.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

TIMEOUT = 20


def strategy_requests(url):
    """Strategy 1: requests (urllib3 TLS stack) with browser headers."""
    try:
        import requests
        session = requests.Session()
        session.headers.update({**HEADERS, "Accept-Encoding": "gzip, deflate"})
        resp = session.get(url, timeout=TIMEOUT, allow_redirects=True)
        if resp.status_code == 200:
            return resp.text
        print(f"[strategy 1/requests] HTTP {resp.status_code}", file=sys.stderr)
    except Exception as e:
        print(f"[strategy 1/requests] {e}", file=sys.stderr)
    return None


def strategy_httpx(url):
    """Strategy 2: httpx with HTTP/2 (ALPN h2 — distinct TLS fingerprint)."""
    try:
        import httpx
        with httpx.Client(http2=True, follow_redirects=True, timeout=TIMEOUT) as client:
            resp = client.get(url, headers=HEADERS)
            if resp.status_code == 200:
                return resp.text
            print(f"[strategy 2/httpx] HTTP {resp.status_code}", file=sys.stderr)
    except Exception as e:
        print(f"[strategy 2/httpx] {e}", file=sys.stderr)
    return None


def strategy_curl(url):
    """Strategy 3: system curl (macOS SecureTransport — third TLS fingerprint)."""
    try:
        cmd = [
            "curl", "--silent", "--fail", "--location", "--compressed",
            "--max-time", str(TIMEOUT),
        ]
        for key, value in HEADERS.items():
            cmd.extend(["--header", f"{key}: {value}"])
        cmd.append(url)

        result = subprocess.run(cmd, capture_output=True, timeout=TIMEOUT + 5)
        if result.returncode == 0:
            return result.stdout.decode("utf-8", errors="replace")
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        print(f"[strategy 3/curl] exit {result.returncode}: {stderr}", file=sys.stderr)
    except Exception as e:
        print(f"[strategy 3/curl] {e}", file=sys.stderr)
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_html.py <URL>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith(("http://", "https://")):
        print(f"Error: URL must start with http:// or https:// (got: {url!r})", file=sys.stderr)
        sys.exit(1)

    for strategy in (strategy_requests, strategy_httpx, strategy_curl):
        html = strategy(url)
        if html:
            print(html, end="")
            sys.exit(0)

    print(
        "\nAll three fetch strategies failed.\n"
        "The site is likely behind Cloudflare or a similar bot-protection system.\n"
        "Fetch the page manually in a browser and paste the HTML directly.",
        file=sys.stderr,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
