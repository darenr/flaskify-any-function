# flaskify-any-function

Any python function (function.py) can be front-ended with flask using a readline/print loop

# Run

`python test_runner.py function.fn 12`

where `function.fn` is `function.py::fun(12)`

`python test_runner.py iris.score 5.8 2.7 5.1 1.9`

or use the flask app

`python app.py`

curl -X POST "http://localhost:5000/app/fn/iris.score" -H "accept: application/json" -H "Content-Type: application/json" -d "[ 5.8, 2.7, 5.1, 1.9]"
