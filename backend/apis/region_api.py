from typing import Dict, List

from flask import request
from flask_restx import Resource

from apis import api, db
from apis.data_models.region_model import region_params, RegionModel, region_update_params
from error_handler import HandleExceptions


class Regions(Resource):
    def get(self, country_id: int) -> List:
        """Get all region in country"""
        try:
            regions = RegionModel.query.filter_by(country_id=country_id).all()
            regions = RegionModel.serialize_list(regions)
            data_return = {
                "Regions": regions
            }
            return data_return
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.doc(body=region_update_params)
    @api.marshal_with(region_params, code=201, envelope="regions", skip_none=True)
    def post(self, country_id: int) -> Dict:
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
    @api.marshal_with(region_params, code=200, envelope="region")
    def get(self, country_id: int, region_id: int) -> Dict:
        """Get region"""
        try:
            region = RegionModel.query.filter(
                RegionModel.id == region_id,
                RegionModel.country_id == country_id
            ).first()
            data_return = {
                "Regions": region.serialize()
            }
            return data_return
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.doc(region_update_params)
    @api.marshal_with(region_update_params, code=202, envelope="region", skip_none=True)
    def put(self, country_id: int, region_id: int) -> Dict:
        """Update region"""
        try:
            region = RegionModel.query.filter(
                RegionModel.id == region_id,
                RegionModel.country_id == country_id
            ).first()
            data = request.get_json()
            region.set_data(data)
            db.session.commit()
            return region
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.marshal_with(region_params, code=202, envelope="region")
    def delete(self, country_id: int, region_id: int) -> Dict:
        """Delete a region"""
        try:
            country_to_delete = RegionModel.query.filter(
                RegionModel.id == region_id,
                RegionModel.country_id == country_id
            ).first()
            db.session.delete(country_to_delete)
            db.session.commit()
            return country_to_delete
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)
