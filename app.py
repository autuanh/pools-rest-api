from flask import Flask, request
from utils import calculate_quantile, load_pool_data, save_pool_data
import os

app = Flask(__name__)
POOL_DATA_FILEPATH = os.path.realpath(os.path.dirname(__file__)) + '/pool_data.json'

# Load pool data file into pools.
pools = load_pool_data(POOL_DATA_FILEPATH)


@app.post("/pools/append")
def append_pool():
    """Appends values to an existing pool or creates a new pool."""

    request_body = request.get_json()

    if request_body['poolId'] not in [pool['poolId'] for pool in pools]:
        pools.append(request_body)

        # Insert a new pool
        message = "inserted"

    else:
        for pool in pools:
            if request_body['poolId'] == pool['poolId']:
                pool['poolValues'].extend(request_body['poolValues'])

        # Append to an existing pool
        message = "appended"

    # Write results to pool_data.json
    save_pool_data(POOL_DATA_FILEPATH, pools)

    return {"message": message,
            "pools": pools}


@app.post("/pools/query")
def query_pool():
    """Queries a pool for a given percentile."""

    request_body = request.get_json()

    for pool in pools:
        if request_body['poolId'] == pool['poolId']:
            pool_values = pool['poolValues']
            quantile_value = calculate_quantile(pool_values, request_body['percentile'])
            return {"Calculated quantile": quantile_value,
                    "Total count of elements": len(pool_values)}
    raise ValueError("Pool not found")


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True)
