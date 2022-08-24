from flask import request
from flask_restx import Resource

from apis import api, db
from apis.data_models.country_model import CountryModel, country_details, country
from error_handler import HandleExceptions


class Countries(Resource):
    @api.marshal_list_with(country_details, code=200, envelope="Countries", description="Get all countries")
    def get(self):
        """ Get all countries """
        countries = CountryModel.query.all()
        return countries

    @api.marshal_with(country, code=201, envelope="country")
    def post(self):
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
    @api.marshal_with(country_details, code=201, envelope="country")
    def put(self, _id):
        """Update country"""
        try:
            _country = CountryModel.query.get_or_404(_id)
            data = request.get_json()
            _country.set_data(data)
            db.session.commit()
            return _country, 200
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.marshal_with(country_details, code=201, envelope="country")
    def get(self, _id):
        """Get country by id"""
        try:
            _country = CountryModel.query.get_or_404(_id)
            return _country, 200
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)

    @api.marshal_with(country_details, envelope="country_deleted", code=200)
    def delete(self, _id):
        """Delete a country"""
        try:
            country_to_delete = CountryModel.query.get_or_404(_id)
            db.session.delete(country_to_delete)
            db.session.commit()
            return country_to_delete, 200
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)


class CountrySearch(Resource):
    @api.marshal_list_with(country_details, code=200, envelope="Countries")
    def get(self):
        """Search country by name"""
        try:
            data = request.args.to_dict()
            name = data.values()
            search = f"%{','.join(name)}%"
            country_detail = CountryModel.query.filter(CountryModel.country.like(search)).all()
            return country_detail
        except Exception as err:
            return HandleExceptions().exception_to_http_response(err)
