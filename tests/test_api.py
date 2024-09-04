import tempfile
from flask_testing import TestCase
from app import app
from unittest.mock import patch


class TestAPI(TestCase):
    def setUp(self):
        app.config["DEBUG"] = True
        app.config["TESTING"] = True

    def create_app(self):
        return app

    @patch(
        "pools.Pools.data_filepath",
        tempfile.NamedTemporaryFile(suffix=".json").name,
    )
    def test_insert_to_new_pool(self):
        """Tests the behavior of append_pool function.

        Expected outputs:
            A post request to create a new pool with pool id 41 and pool values of [1, 2, 3, 4, 5]
            should return status code 200 with message 'inserted'.
        """
        response = self.client.post(
            "/pools/append",
            json={"poolId": 41, "poolValues": [1, 2, 3, 4, 5]},
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "inserted"})

    @patch(
        "pools.Pools.data_filepath",
        tempfile.NamedTemporaryFile(suffix=".json").name,
    )
    def test_append_to_existing_pool(self):
        """Tests the behavior of append_pool function.

        Expected outputs:
            - The first post request should create a new pool with pool id 42 and pool values of [11, 12, 13, 14]
            and return status code 200 with message 'inserted'.
            - The second post request should append pool values of [15, 16, 17, 18] to pool id 42
            and return status code 200 with message 'appended'.
        """

        response_1 = self.client.post(
            "/pools/append",
            json={"poolId": 42, "poolValues": [11, 12, 13, 14]},
            headers={"Content-Type": "application/json"},
        )

        response_2 = self.client.post(
            "/pools/append",
            json={"poolId": 42, "poolValues": [15, 16, 17, 18]},
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_1.json, {"message": "inserted"})
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_2.json, {"message": "appended"})

    @patch(
        "pools.Pools.data_filepath",
        tempfile.NamedTemporaryFile(suffix=".json").name,
    )
    def test_query_pool_happy_case(self):
        """Tests the behavior of query_pool function with an existent pool id.

        Expected outputs:
            - The first post request should create a new pool with pool id 43 and pool values of [1, 2, 3, 4, 5]
            and return status code 200 with message 'inserted'.
            - The second post request to query for pool id 43 and 50th percentile should return status code 200,
            with calculated percentile value is 5 and total count of values in pool is 5.
        """
        response_v1 = self.client.post(
            "/pools/append",
            json={"poolId": 43, "poolValues": [1, 3, 5, 7, 9]},
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response_v1.status_code, 200)
        self.assertEqual(response_v1.json, {"message": "inserted"})

        response_v2 = self.client.post(
            "/pools/query",
            json={"poolId": 43, "percentile": 50},
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response_v2.status_code, 200)
        self.assertEqual(
            response_v2.json,
            {"Calculated percentile value": 5, "Total count of elements": 5},
        )

    def test_query_pool_not_found(self):
        """Tests the behavior of query_pool function with a non-existent pool id.

        Expected outputs:
            A post request to query for pool id 100 and 50th percentile should raise a ValueError ('Pool not found').
        """
        with self.assertRaises(ValueError):
            self.client.post(
                "/pools/query",
                json={"poolId": 44, "percentile": 50},
                headers={"Content-Type": "application/json"},
            )
