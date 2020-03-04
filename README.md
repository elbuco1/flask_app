# Sample python flask API deployed using Docker, Nginx, Gunicorn and MySQL

## App architecture

The app Movies allows to manage movie informations. Each movie has two attributes: the movie name and its release year. The service is implemented as a REST API. All required requests are implemented.

## Run locally in a python virtualenv
* Clone repository: <code>$ git clone https://github.com/elbuco1/flask_app.git</code>
* To start the app, go in the **flask_app** directory: <code>$ cd flask_app</code>
* If you want to use a mysql database instead of sqlite then install mysql: https://virtualzero.net/blog/install-mysql-for-a-flask-app-on-ubuntu-18.04-lts

* If you are using mysql database you need to create a user and a database as follows:

In your terminal: <code>$ sudo mysql -u root -p</code>

In the mysql command line:

<code>mysql> CREATE DATABASE movies; </code>

<code>mysql> CREATE USER 'movies'@'localhost' IDENTIFIED BY 'movies'; </code>

<code>mysql> GRANT ALL PRIVILEGES ON movies.* TO 'movies'@'localhost'; </code>

<code>mysql> FLUSH PRIVILEGES; </code>



* If you want to use the sqlite db, then go in **config.py** and set
```python
class Config(object):
    deploy = 'sqlite_local'
```
* If you want to use the mysql database, then go in **config.py** and set
```python
class Config(object):
    deploy = 'mysql_local'
```
* Create a python3 virtual environment: <code>$ python3 -m venv movies</code>
* Activate the environment: <code>$ source movies/bin/activate</code>
* Update pip: <code>$pip install --upgrade pip wheel</code>
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
To run the app using nginx as web server, gunicorn as application server
and mysql server. 
* Clone repository: <code>$ git clone https://github.com/elbuco1/flask_app.git</code>
* To start the app, go in the **flask_app** directory: <code>$ cd flask_app</code>
* Install docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* Install docker-compose: https://docs.docker.com/compose/install/
* Go in **config.py** and set
```python
class Config(object):
    deploy = 'docker'
```
Then run:
<code>$ sudo docker-compose up nginx </code>

or 

<code>$ sudo docker-compose up -d nginx </code> 

to run the containers in the background.

You can find the app on "http://127.0.0.1/movies"

## Stopping all docker containers:

To shutdown the app:
<code>$ sudo docker-compose down</code> 

To stop all containers:
<code>$ sudo docker stop $(sudo docker ps -a -q)</code> 

To remove all containers:

<code>$ sudo docker rm $(sudo docker ps -a -q)</code> 


