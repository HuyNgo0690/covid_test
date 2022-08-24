from flask_restx import fields
from sqlalchemy import inspect

from apis import db, api
from apis.data_models.base import BaseMode

country = api.model(
    'Country',
    {
        'id': fields.Integer(),
        'recovered': fields.Integer(required=True, min=0),
        'deaths': fields.Integer(required=True, min=0),
        'confirmed': fields.Integer(required=True, min=0),
        'country': fields.String(required=False),
        'population': fields.Integer(required=False),
        'sq_km_area': fields.Integer(required=False),
        'life_expectancy': fields.String(required=False),
        'elevation_in_meters': fields.String(required=False),
        'continent': fields.String(required=False),
        'abbreviation': fields.String(required=False),
        'location': fields.String(required=False),
        'iso': fields.Integer(required=False),
        'capital_city': fields.String(required=False),
        'lat': fields.String(required=False),
        'long': fields.String(required=False),
        'updated': fields.String(required=False)
    }
)


class CountryModel(BaseMode, db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer(), primary_key=True)
    country = db.Column(db.String(200), nullable=True)
    recovered = db.Column(db.BigInteger(), nullable=True)
    confirmed = db.Column(db.BigInteger(), nullable=True)
    deaths = db.Column(db.BigInteger(), nullable=True)
    population = db.Column(db.BigInteger(), nullable=True)
    sq_km_area = db.Column(db.BigInteger(), nullable=True)
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
