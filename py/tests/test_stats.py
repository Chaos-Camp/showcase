import unittest

from shortlink.stats import total_clicks


class TotalClicks(unittest.TestCase):
    def test_counts_only_clicks(self):
        events = [{"kind": "click"}, {"kind": "view"}, {"kind": "click"}]
        self.assertEqual(total_clicks(events), 2)
