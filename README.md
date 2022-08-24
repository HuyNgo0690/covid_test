# Covid API
This is a project I used REST APIs with Flask and Flask-Restx and SqlAlchedmy


# How to run the project
After pull repo from git.
cd to your repo and then run:
docker-compose up -d --build
After finished, open browser and go to localhost:3001. This is a Swagger, which will show API Documentation.
To initialize data in database. Use API: 

localhost:3001/init_db -> Body will be binary, which you can select json file. I handle following sample json.