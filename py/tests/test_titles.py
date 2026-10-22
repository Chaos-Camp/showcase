import unittest

import requests

from shortlink.report import weekly
from shortlink.titles import title_of


class Page:
    def __init__(self, status, text=""):
        self.status_code, self.text = status, text


class Titles(unittest.TestCase):
    def test_a_title_on_one_line(self):
        page = Page(200, "<html><head><title>\n  Launch notes &amp; FAQ\n</title></head></html>")
        self.assertEqual(title_of("https://example.com", get=lambda url, timeout: page), "Launch notes & FAQ")

    def test_no_title_when_the_page_fails(self):
        self.assertIsNone(title_of("https://example.com", get=lambda url, timeout: Page(404)))

        def down(url, timeout):
            raise requests.ConnectionError("down")

        self.assertIsNone(title_of("https://example.com", get=down))

    def test_the_report_shows_titles(self):
        text = weekly([{"kind": "click", "slug": "launch-notes"}], "2026-10-19", titles={"launch-notes": "Launch notes"})
        self.assertIn("Launch notes", text)
