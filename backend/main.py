import datetime
import logging.config

from apis import api, db, app
from config.config import Config

logging.config.fileConfig(Config.LOGGING_CONF, disable_existing_loggers=False)
logger = logging.getLogger(Config.LOGGER)

from apis.data_models.country_model import CountryModel
from apis.data_models.region_model import RegionModel
from apis.region_api import Regions, Region
from apis.country_api import Countries, CountryResource, CountrySearch
from apis.init_data import DataInit
from apis.middleware import middleware

api.add_resource(Countries, "/countries")
api.add_resource(CountryResource, "/country/<int:country_id>")
api.add_resource(CountrySearch, "/countries/search")
api.add_resource(Regions, "/country/<int:country_id>/region")
api.add_resource(Region, "/country/<int:country_id>/region/<int:region_id>")
api.add_resource(DataInit, "/init_data")
db.create_all()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Country': CountryModel,
        'Region': RegionModel
    }


@app.after_request
def after_request(response):
    logger.info(response)
    return response


logger.info(f"Backend server start at {datetime.datetime.now()}")
if __name__ == '__main__':
    from waitress import serve

    serve(app, host='0.0.0.0', port=Config.APP_PORT)
    # app.run(debug=True, port=Config.APP_PORT)
