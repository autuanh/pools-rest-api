import tempfile
from flask_testing import TestCase
from app import app
from utils import calculate_percentile, load_pool_data
from unittest.mock import patch, mock_open


class TestAPI(TestCase):
    def setUp(self):
        app.config['DEBUG'] = True
        app.config['TESTING'] = True

    def create_app(self):
        return app

    @patch("app.POOL_DATA_FILEPATH", tempfile.NamedTemporaryFile(suffix='.json', delete=True).name)
    def test_append_pool(self):
        response = self.client.post('/pools/append',
                                    json={'poolId': 99, 'poolValues': [1, 2, 3, 4]},
                                    headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_calculate_percentile(self):
        self.assertEqual(calculate_percentile([1, 2, 3, 4], 50), 2.5)
        self.assertEqual(calculate_percentile(range(150), 70), 104.3)
        self.assertEqual(calculate_percentile(range(165), 90), 147.6)

    def test_query_pool_case_1(self):
        response = self.client.post('/pools/query', json={'poolId': 99, 'percentile': 50},
                                    headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"Calculated quantile": 2.5,
                                         "Total count of elements": 4})

    def test_query_pool_case_2(self):
        with self.assertRaises(ValueError):
            self.client.post('/pools/query',
                             json={'poolId': 100, 'percentile': 50},
                             headers={'Content-Type': 'application/json'})
