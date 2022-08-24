from data_models.base import BaseMode
from __main__ import db, api
from flask_restx import fields

country_params = api.model(
    'Country',
    {
        'id': fields.Integer(),
        'recovered': fields.String(required=True),
        'deaths': fields.String(required=True),
        'confirmed': fields.String(required=True),
        'region': fields.Integer(required=False),
        'country': fields.String(required=True),
        'population': fields.String(required=True),
        'sq_km_area': fields.String(required=True),
        'life_expectancy': fields.String(required=True),
        'elevation_in_meters': fields.String(required=True),
        'continent': fields.String(required=True),
        'abbreviation': fields.String(required=True),
        'location': fields.String(required=True),
        'iso': fields.String(required=True),
        'capital_city': fields.String(required=True),
        'lat': fields.String(required=True),
        'long': fields.String(required=True),
        'updated': fields.String(required=True)
    }
)


class CountryModel(BaseMode, db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer(), primary_key=True)
    country = db.Column(db.String(200), nullable=True)
    recovered = db.Column(db.String(200), nullable=True)
    confirmed = db.Column(db.String(200), nullable=True)
    deaths = db.Column(db.String(200), nullable=True)
    population = db.Column(db.Integer, nullable=True)
    sq_km_area = db.Column(db.Integer, nullable=True)
    life_expectancy = db.Column(db.String(80), nullable=True)
    elevation_in_meters = db.Column(db.String(80), nullable=True)
    continent = db.Column(db.String(80), nullable=True)
    abbreviation = db.Column(db.String(10), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    iso = db.Column(db.Integer, nullable=True)
    capital_city = db.Column(db.String(80), nullable=True)
    lat = db.Column(db.String(80), nullable=True)
    long = db.Column(db.String(80), nullable=True)
    updated = db.Column(db.String(80), nullable=True)
    db.UniqueConstraint(country)
