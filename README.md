# Building a REST API with Python 3

## Getting started

To make it easy for you to get started with the project, follow the steps in the setup instructions below.

## Setup instructions

### 1. Clone this repository

Open a terminal and run the following command:
```
git clone https://github.com/autuanh/pools-rest-api.git
```

### 2. Set up virtual environment

- Navigate to the repository you have cloned
```
cd pools-rest-api
```

- Create and activate virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

- Install required packages
```
python3 -m pip install -r requirements.txt
```

### 3. Run the project
- To start the application, run the following command:
```
python app.py
```

- Open another terminal and run the following commands:

3.1. Append or insert data to pools

For example:
```
curl -i http://127.0.0.1:5000/pools/append \
-X POST \
-H 'Content-Type: application/json' \
-d '{"poolId":1, "poolValues": [88, 34, 65, 12, 56, 22, 88]}'
```

You should see something like this:
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.4 Python/3.12.5
Date: Wed, 04 Sep 2024 09:27:29 GMT
Content-Type: application/json
Content-Length: 28
Connection: close

{
  "message": "inserted"
}
```

3.2. Query percentile value from a pool

For example:
```
curl -i http://127.0.0.1:5000/pools/query \
-X POST \
-H 'Content-Type: application/json' \
-d '{"poolId":1, "percentile": 55.96}'
```

You should see something like this:
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.4 Python/3.12.5
Date: Wed, 04 Sep 2024 09:27:37 GMT
Content-Type: application/json
Content-Length: 75
Connection: close

{
  "Calculated percentile value": 59.22,
  "Total count of elements": 7
}
```
