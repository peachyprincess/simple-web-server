# A simple web application 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

The application was written with Python/Flask. The server accepts a POST request to the route "/test", which accepts one argument "string_to_cut" and return a JSON object with the key "return_string" and a string containing every third letter from the original string. For example, if you POST {"string_to_cut": "iamyourlyftdriver"}, it should return {"return_string": "muydv"}.

## Setup dependency

I followed this [guide](https://phoenixnap.com/kb/install-flask) to set up a virtual environment with python3. You can ctivate the Environment on Linux and OS X by running 
```
. flask/env/bin/activate
```

## Running and testing the server
You can run the server by
```
$> FLASK_APP=app.py flask run
 * Serving Flask app 'app.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Then you can open another terminal window to run the test client (while keeping the server up) with
```
$> python test_client.py http://127.0.0.1:5000
input: {'string_to_cut': 'hello,world'}, output: {'return_string': 'l,r'}
input: {'string_to_cut': 'iamyourlyftdriver'}, output: {'return_string': 'muydv'}
```
If the second argument is not specified, `http://127.0.0.1:5000` will be used as the default endpoint. You should also see the POST request on the server side.
```
$>  FLASK_APP=app.py flask run
...
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [18/Jun/2021 08:50:46] "POST /test HTTP/1.1" 200 -
127.0.0.1 - - [18/Jun/2021 08:50:46] "POST /test HTTP/1.1" 200 -
```
