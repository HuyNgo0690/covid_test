from __main__ import api, db

from flask import request
from flask_restx import Resource

from data_models.country_region_model import CountryRegionModel
from data_models.region_model import region_params, RegionModel


class Regions(Resource):
    @api.marshal_list_with(region_params, code=200, envelope="Regions")
    def get(self, country_id):
        regions = RegionModel.query.filter_by(country_id=country_id).all()
        return regions, 200

    @api.marshal_with(region_params, code=200, envelope="Regions")
    def post(self, country_id):
        data = request.get_json()
        data["country_id"] = country_id
        new_region = RegionModel()
        new_region.set_data(data)
        db.session.add(new_region)
        db.session.flush()
        new_country_region = CountryRegionModel(country_id=country_id, region_id=new_region.id)
        db.session.add(new_country_region)
        db.session.commit()
        return new_region
