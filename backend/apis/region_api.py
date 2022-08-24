from flask import request
from flask_restx import Resource

from apis import api, db
from apis.data_models.region_model import region_params, RegionModel
from error_handler import HandleExceptions


class Regions(Resource):
    @api.marshal_list_with(region_params, code=200, envelope="Regions")
    def get(self, country_id):
        """Get all region in country"""
        try:
            regions = RegionModel.query.filter_by(country_id=country_id).all()
            return regions, 200
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.marshal_with(region_params, code=200, envelope="Regions")
    def post(self, country_id):
        """Add new region"""
        try:
            data = request.get_json()
            data["country_id"] = country_id
            new_region = RegionModel()
            new_region.set_data(data)
            db.session.add(new_region)
            db.session.commit()
            return new_region
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)


class Region(Resource):
    @api.marshal_with(region_params, code=201, envelope="country")
    def put(self, _id):
        """Update region"""
        try:
            region = RegionModel.query.get_or_404(_id)
            data = request.get_json()
            region.set_data(data)
            db.session.commit()
            return region, 200
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.marshal_with(region_params, code=201, envelope="country_deleted")
    def delete(self, region_id):
        """Delete a region"""
        try:
            country_to_delete = RegionModel.query.get_or_404(region_id)
            db.session.delete(country_to_delete)
            db.session.commit()
            return country_to_delete, 200
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)
