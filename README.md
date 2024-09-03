# Building a REST API with Python 3

## Getting started

To make it easy for you to get started with the project, follow the steps in the setup instructions below.

## Setup instructions

### 1. Clone this repository

For this you run: 
```
https://github.com/autuanh/pools-rest-api.git
```

### 2. Set up virtual environment
- Open a terminal and navigate to the directory. Then, run the following command:
```
python -m venv .venv
```
- To start using the virtual environment, activate it:
```
source .venv/bin/activate
```

### 3. Install all of the packages needed by the environment
```
pip install -r requirements.txt
```

### 4. Run the project
- To start the application, run the following command:
```
python app.py
```

- Append or insert data to pools

For example:
```
curl -i http://127.0.0.1:5000/pools/append \
-X POST \
-H 'Content-Type: application/json' \
-d '{"poolId":1, "poolValues": [1,2,3,4,5]}'
```

- Query percentile value from a pool

For example:
```
curl -i http://127.0.0.1:5000/pools/query \
-X POST \
-H 'Content-Type: application/json' \
-d '{"poolId":1, "percentile": 50}'
```
