# Building a REST API with Python 3

## Setup instructions

1. Set up virtual environment
- Open a terminal and navigate to the directory. Then, run the following command:
python -m venv venv
- To start using the virtual environment, activate it:
source venv/bin/activate

2. 

### To append or insert data to pools

curl -i http://127.0.0.1:5000/pools/append \
-X POST \
-H 'Content-Type: application/json' \
-d '{"poolId":1, "poolValues": [1,2,3,4,5]}'

### To query percentile value from a pool

curl -i http://127.0.0.1:5000/pools/query \
-X POST \
-H 'Content-Type: application/json' \
-d '{"poolId":1, "percentile": 50}'

