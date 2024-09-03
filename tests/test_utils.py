from unittest import TestCase
from utils import calculate_percentile


class TestUtils(TestCase):
    def test_calculate_percentile(self):
        self.assertEqual(calculate_percentile([1, 2, 3, 4], 50), 2.5)
        self.assertEqual(calculate_percentile(range(150), 70), 104.3)
        self.assertEqual(calculate_percentile(range(165), 90), 147.6)
