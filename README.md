# Covid API
This project I used REST APIs with Flask and Flask-Restx and Flask-SqlAlchemy, PostgresSQL. I used 2 dockers, one for backend, and one for database. </br>
At the initialize, flask-sqlAlchemy will auto create database and table. We have 2 tables: Country and Region, with one to many relationship(Country 1:n Region).</br>

To run this project, you need to install docker and docker-compose. I assuming you know how to install docker and docker-compose, so skip the installation instruction.
# How to run the project
__After pull repo from git. Then:__<br/>
```
cd <your_repo_dir>
docker-compose up -d --build
```
After the process is finished, open browser and go to localhost:3001. This is a Swagger, which will show API Documentation. </br>
Use postman to run API. </br>
To initialize data in database. Use API: 

> localhost:3001/init_db -> Body will be a file, which you can select json file(Ex: covid-stats.json).
