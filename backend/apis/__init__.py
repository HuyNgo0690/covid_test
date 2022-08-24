from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from apis.middleware.middleware import Middleware
from config.config import Config

app = Flask(__name__)
api = Api()

app.wsgi_app = Middleware(app.wsgi_app)

api.init_app(app, doc='/', title="Covid API", description="A simple REST API for covid")
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@{Config.POSTGRES_HOST}:{Config.POSTGRES_PORT}/{Config.POSTGRES_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RESTX_VALIDATION'] = True

db = SQLAlchemy(app)
