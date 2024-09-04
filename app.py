from flask import Flask, request
from utils import calculate_percentile
from pools import Pools

app = Flask(__name__)

# Load pool data file into pools.
pools = Pools.load()


@app.post("/pools/append")
def append_pool() -> dict:
    """Handles a post request containing a JSON document with 2 fields: 'poolId' (int) and 'poolValues' (list of ints).
    Appends values to an existing pool or creates a new pool, then saves new pool data to a JSON file

    Inputs:
        - request: a flask.Request object
        Reference: https://tedboy.github.io/flask/generated/generated/flask.Request.html
    Returns:
        - dict: contain a message ('inserted' or 'appended')
    """
    request_body = request.get_json()

    if request_body["poolId"] not in [pool["poolId"] for pool in pools]:
        pools.append(request_body)

        # Insert a new pool
        message = "inserted"

    else:
        for pool in pools:
            if request_body["poolId"] == pool["poolId"]:
                pool["poolValues"].extend(request_body["poolValues"])

        # Append to an existing pool
        message = "appended"

    # Write results to pool_data.json
    Pools.save(pools)

    return {"message": message}


@app.post("/pools/query")
def query_pool() -> dict:
    """Handles a post request containing a JSON document with 2 fields: 'poolId' (int) and 'percentile' (float).
    Queries and returns a percentile value and number of elements from the given pool.

    Inputs:
        - request: a flask.Request object
        Reference: https://tedboy.github.io/flask/generated/generated/flask.Request.html
    Returns:
        - dict: contain a calculated percentile value and number of elements from the given pool.
    """
    request_body = request.get_json()

    for pool in pools:
        if request_body["poolId"] == pool["poolId"]:
            pool_values = pool["poolValues"]
            percentile_value = calculate_percentile(
                pool_values, request_body["percentile"]
            )
            return {
                "Calculated percentile value": percentile_value,
                "Total count of elements": len(pool_values),
            }
    raise ValueError("Pool not found")


if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.config["TESTING"] = True
    app.run(debug=True)
