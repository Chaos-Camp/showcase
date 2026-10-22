"""Page titles, for a report that says which page a slug was."""

import html
import re

import requests

TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def title_of(url, get=requests.get, timeout=5):
    """The page's <title>, unescaped and on one line; None when the page has none or will not load."""
    try:
        response = get(url, timeout=timeout)
    except requests.RequestException:
        return None
    if response.status_code != 200:
        return None
    match = TITLE.search(response.text)
    return " ".join(html.unescape(match.group(1)).split()) if match else None
