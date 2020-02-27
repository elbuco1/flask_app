# Sample microservices architecture using python flask and sql alchemy

## Global architecture

There are two services:
* Movies: allows to manage movie informations. Each movie has two attributes: the movie name and its release year. The service is implemented as a REST API. All required requests are implemented.
* Evaluations: allows to manage the movie evaluations. Each movie can have any number of evaluation. An evaluation has two attributes: the description and the evaluated movie id. The service is implemented as a REST API. All required requests are implemented.

The two services interact through HTTP protocol for some of the requests.

## Movies service

### Run
* Clone repository: <code>$ git clone https://github.com/elbuco1/microservices.git</code>
* To start the micro-service, go in the **movies** directory: <code>$ cd microservices/movies</code>
* Create a python3 virtual environment: <code>$ python3 -m venv movies_service</code>
* Activate the environment: <code>$ source movies_service/bin/activate</code>
* Install dependencies from requirements.txt file:<code>$ pip install -r requirements.txt</code>
* Initialize the database:<code>$ flask initdb</code>
* Run the server: <code>$ flask run</code>

Movies service runs on http://127.0.0.1:5000/

### Test
To list all available routes you can run <code>$ flask routes</code>

To test the different routes you can do as follows:
* Open a new python terminal : <code>$ python</code>
* To create a simple GET request use the code below:
```python
import requests
# Create request
request = "http://127.0.0.1:5000/movies/"
# Send get request
response = requests.get(request)
# View returned json
response.json()
```
* More complex requests such as POST or PUT need data to be send as json:
```python
import requests
# Create request
request = "http://127.0.0.1:5000/movies/add"
# Create json data
data = {"name": "la cite de la peur", "year":1994}
# Send get request
response = requests.post(request, json = data)
# View returned json
response.json()
```


## Evaluations service
Open another terminal:
### Run
* Clone repository: <code>$ git clone https://github.com/elbuco1/microservices.git</code>
* To start the micro-service, go in the **movies** directory: <code>$ cd microservices/evaluations</code>
* Create a python3 virtual environment: <code>$ python3 -m venv evaluations_service</code>
* Activate the environment: <code>$ source evaluations_service/bin/activate</code>
* Install dependencies from requirements.txt file:<code>$ pip install -r requirements.txt</code>
* Initialize the database:<code>$ flask initdb</code>
* Run the server: <code>$ flask run</code>

Movies service runs on http://127.0.0.1:5001/

### Test
To list all available routes you can run <code>$ flask routes</code>

To test the different routes you can do as follows:
* Open a new python terminal : <code>$ python</code>
* To create a simple GET request use the code below:
```python
import requests
# Create request
request = "http://127.0.0.1:5001/evaluations/"
# Send get request
response = requests.get(request)
# View returned json
response.json()
```
* More complex requests such as POST or PUT need data to be send as json:
```python
import requests
# Create request
movie_id = 1
request = "http://127.0.0.1:5001//evaluations/add/{}".format(movie_id)
# Create json data
data = {"description": "This is a goood movie!"}
# Send get request
response = requests.post(request, json = data)
# View returned json
response.json()
```

## Server parameters
For now microservies are run on localhost.
* Server is set in the file **app/.flaskenv**.
* To set the debug mode to false, remove the line: <code>$ FLASK_ENV=development</code>
* To set the port, change the line: <code>$ FLASK_RUN_PORT=5000</code>