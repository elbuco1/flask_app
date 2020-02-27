# Sample python flask API deployed using Docker, Nginx, Gunicorn and MySQL

## App architecture

The app Movies allows to manage movie informations. Each movie has two attributes: the movie name and its release year. The service is implemented as a REST API. All required requests are implemented.

## Run locally in a python virtualenv
* Clone repository: <code>$ git clone https://github.com/elbuco1/flask_app.git</code>
* To start the app, go in the **flask_app** directory: <code>$ cd flask_app</code>
* Create a python3 virtual environment: <code>$ python3 -m venv movies</code>
* Activate the environment: <code>$ source movies/bin/activate</code>
* Install dependencies from requirements.txt file:<code>$ pip install -r requirements.txt</code>
* Initialize the database:<code>$ flask initdb</code>
* Run the server: <code>$ flask run</code>

Movies service runs on http://127.0.0.1:5000/
### Server parameters
For now microservies are run on localhost.
* Server is set in the file **app/.flaskenv**.
* To set the debug mode to false, remove the line: <code>$ FLASK_ENV=development</code>
* To set the port, change the line: <code>$ FLASK_RUN_PORT=5000</code>


## Test
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
## Deploy using Docker, Nginx, Gunicorn and MySQL


