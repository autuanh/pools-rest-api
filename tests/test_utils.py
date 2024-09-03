from unittest import TestCase
from utils import calculate_quantile


class TestUtils(TestCase):
    def test_calculate_quantile(self):
        """Test the behavior of calculate_quantile function.

        Test cases:
            - Quantile value of a list from 1 to 4 for 50th percentile should return 2.5.
            - Quantile value of a list from 0 to 149 for 70th percentile should return 104.3.
            - Quantile value of a list from 0 to 164 for 50th percentile should return 147.6.
        """
        self.assertEqual(calculate_quantile([1, 2, 3, 4], 50), 2.5)
        self.assertEqual(calculate_quantile(range(150), 70), 104.3)
        self.assertEqual(calculate_quantile(range(165), 90), 147.6)
