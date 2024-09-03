import tempfile
from flask_testing import TestCase
from app import app
from unittest.mock import patch


class TestAPI(TestCase):
    def setUp(self):
        app.config['DEBUG'] = True
        app.config['TESTING'] = True

    def create_app(self):
        return app

    @patch("app.POOL_DATA_FILEPATH", tempfile.NamedTemporaryFile(suffix='.json', delete=True).name)
    def test_append_pool(self):
        """Tests the behavior of append_pool function.

          Test case:
              Response content of a request to append or insert a pool with pool id is 99 and pool values
              of [1, 2, 3, 4] should return status code 200.
        """
        response = self.client.post('/pools/append',
                                    json={'poolId': 99, 'poolValues': [1, 2, 3, 4]},
                                    headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_query_pool_case_1(self):
        """Tests the behavior of query_pool function with an existent pool id.

        Test case:
            - Response content of a request to query pool with pool id is 99 for 50th percentile
            should return status code 200.
            - Response content of a request to query pool with pool id is 99 for 50th percentile
            should return calculated quantile is 2.5 and total count of values in pool is 4.
        """
        response = self.client.post('/pools/query', json={'poolId': 99, 'percentile': 50},
                                    headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"Calculated quantile": 2.5,
                                         "Total count of elements": 4})

    def test_query_pool_case_2(self):
        """Tests the behavior of query_pool function with a non-existent pool id.

        Test case:
            Response content of a request to query pool with pool id is 100 for 50th percentile
            should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.client.post('/pools/query',
                             json={'poolId': 100, 'percentile': 50},
                             headers={'Content-Type': 'application/json'})
