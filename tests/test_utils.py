from unittest import TestCase
from utils import calculate_percentile


class TestUtils(TestCase):
    def test_calculate_quantile(self):
        """Test the behavior of calculate_percentile function.

        Test cases:
            - Case 1: Calculating the 50th percentile value of [1, 2, 3, 4] should return 2.5.
            - Case 2: Calculating the 70th percentile value of [21, 45, 6, 58, 23] should return 40.6.
            - Case 3: Calculating the 55.96th percentile value of [88, 34, 65, 12, 56, 22, 88] should return 59.22.
        """
        self.assertEqual(calculate_percentile([1, 2, 3, 4], 50), 2.5)
        self.assertEqual(calculate_percentile([21, 45, 6, 58, 23], 70), 40.6)
        self.assertEqual(
            calculate_percentile([88, 34, 65, 12, 56, 22, 88], 55.96), 59.22
        )
