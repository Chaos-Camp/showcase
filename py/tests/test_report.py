import unittest

from shortlink.report import busiest, weekly

EVENTS = [
    {"kind": "click", "slug": "launch-notes"},
    {"kind": "click", "slug": "pricing"},
    {"kind": "click", "slug": "launch-notes"},
    {"kind": "view", "slug": "pricing"},
]


class Report(unittest.TestCase):
    def test_busiest_first(self):
        self.assertEqual(busiest(EVENTS), [("launch-notes", 2), ("pricing", 1)])

    def test_the_report_says_the_week_and_the_total(self):
        text = weekly(EVENTS, "2026-10-19")
        self.assertIn("clicks, week of 2026-10-19: 3", text)
        self.assertIn("launch-notes", text)

    def test_a_quiet_week(self):
        self.assertIn("no clicks this week", weekly([], "2026-10-19"))
