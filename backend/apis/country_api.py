from __main__ import api, db

from flask import request
from flask_restx import Resource, abort
from sqlalchemy.exc import IntegrityError

from data_models.country_model import country_params, CountryModel


class Countries(Resource):
    @api.marshal_list_with(country_params, code=200, envelope="Countries")
    def get(self):
        ''' Get all countries '''
        countries = CountryModel.query.all()
        return countries

    @api.marshal_with(country_params, code=201, envelope="country")
    def post(self):
        ''' Create a new country '''
        try:
            all_info = request.get_json()
            new_country = CountryModel()
            new_country.set_data(all_info)
            db.session.add(new_country)
            db.session.commit()
            return new_country
        except IntegrityError:
            abort(400, "Country exist !!!")


class CountryResource(Resource):
    @api.marshal_with(country_params, code=201, envelope="country")
    def put(self, _id):
        try:
            country = CountryModel.query.get_or_404(_id)
            data = request.get_json()
            country.set_data(data)
            db.session.commit()
            return country, 200
        except Exception:
            abort(400, "Unexpected error")

    @api.marshal_with(country_params, code=201, envelope="country")
    def get(self, _id):
        try:
            country = CountryModel.query.get_or_404(_id)
            return country, 200
        except Exception:
            abort(400, "Unexpected error")

    @api.marshal_with(country_params, envelope="country_deleted", code=200)
    def delete(self, _id):
        '''Delete a country'''

        country_to_delete = CountryModel.query.get_or_404(id)
        db.session.delete(country_to_delete)
        db.session.commit()
        return country_to_delete, 200
