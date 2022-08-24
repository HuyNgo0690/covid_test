import json

from flask import request
from flask_restx import Resource

from apis import db, api
from apis.data_models.country_model import CountryModel
from apis.data_models.region_model import RegionModel
from error_handler import HandleExceptions


class DataInit(Resource):
    @api.doc(body={"data": "File json"})
    def post(self):
        """Init data by file"""
        try:
            data = request.get_data().decode('utf8')
            data = json.loads(data)
            for key, value in data.items():
                country_details = value.pop("All")
                country_details["country"] = key
                country_id = self.add_countries(country_details)
                if value:
                    for _key, _val in value.items():
                        region_name = _key
                        region_details = _val
                        region_details["region"] = region_name
                        region_details["country_id"] = country_id
                        self.add_regions(region_details)
            db.session.commit()
            return {"message": "Done"}
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    def add_countries(self, country_details):
        country = CountryModel()
        country.set_data(country_details)
        db.session.add(country)
        db.session.flush()
        return country.id

    def add_regions(self, region_details):
        region = RegionModel()
        region.set_data(region_details)
        db.session.add(region)
