import logging.config
from datetime import datetime

from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from config.config import Config
from middleware.middleware import Middleware

logging.config.fileConfig(Config.LOGGING_CONF, disable_existing_loggers=False)
logger = logging.getLogger(Config.LOGGER)

app = Flask(__name__)
app.wsgi_app = Middleware(app.wsgi_app)
api = Api()
api.init_app(app, doc='/', title="Covid API", description="A simple REST API for covid")
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@{Config.POSTGRES_HOST}:{Config.POSTGRES_PORT}/{Config.POSTGRES_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db)

from data_models.country_model import CountryModel
from data_models.country_region_model import CountryRegionModel
from data_models.region_model import RegionModel
from apis.region_api import Regions
from apis.country_api import Countries, CountryResource

api.add_resource(Regions, "/country/<int:country_id>/region")
api.add_resource(Countries, "/country")
api.add_resource(CountryResource, "/country/<int:_id>")


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Country': CountryModel,
        'Region': RegionModel,
        'CountryRegion': CountryRegionModel,
    }


if __name__ == '__main__':
    logger.info(f"Backend server start at {datetime.now()}")
    app.run(debug=True, port=Config.APP_PORT)
