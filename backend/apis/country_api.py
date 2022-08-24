from typing import Dict, List

from flask import request
from flask_restx import Resource

from apis import api, db
from apis.data_models.country_model import CountryModel, country_params, country_update_params
from apis.data_models.region_model import RegionModel
from error_handler import HandleExceptions


class Countries(Resource):
    def get(self) -> List:
        """ Get all countries """
        try:
            countries = CountryModel.query.all()
            countries = CountryModel.serialize_list(countries)
            data_return = {
                "Countries": countries
            }
            return data_return
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.doc(body=country_update_params, validate=True)
    @api.marshal_with(country_params, code=201, envelope="country", skip_none=True)
    def post(self) -> Dict:
        """ Create a new country """
        try:
            all_info = request.get_json()
            new_country = CountryModel()
            new_country.set_data(all_info)
            db.session.add(new_country)
            db.session.commit()
            return new_country
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)


class CountryResource(Resource):
    @api.doc(body=country_update_params, validate=True)
    @api.marshal_with(country_update_params, code=202, envelope="country", skip_none=True)
    def put(self, country_id: int) -> Dict:
        """Update country"""
        try:
            _country = CountryModel.query.get_or_404(country_id)
            data = request.get_json()
            _country.set_data(data)
            db.session.commit()
            return _country
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    def get(self, country_id: int) -> Dict:
        """Get country by id"""
        try:
            _country = CountryModel.query.filter(CountryModel.id == country_id).first()
            if _country:
                data_return = {
                    "Country": _country.serialize()
                }
                region_list = RegionModel.query.filter(RegionModel.country_id == country_id).all()
                if region_list:
                    region_list = RegionModel.serialize_list(region_list)
                    data_return["Country"]["regions"] = region_list
                return data_return
            else:
                return {"message": "Country not found"}
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.marshal_with(country_params, envelope="country_deleted", code=202)
    def delete(self, country_id: int) -> Dict:
        """Delete a country"""
        try:
            country_to_delete = CountryModel.query.get_or_404(country_id)
            db.session.delete(country_to_delete)
            db.session.commit()
            return country_to_delete
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)


class CountrySearch(Resource):
    def get(self) -> List:
        """Search country by name"""
        try:
            data = request.args.to_dict()
            name = data.values()
            search = f"%{','.join(name)}%"
            country_detail = CountryModel.query.filter(CountryModel.country.ilike(search)).all()
            country_detail = CountryModel.serialize_list(country_detail)
            data_return = {
                "Countries": country_detail
            }
            return data_return
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)
