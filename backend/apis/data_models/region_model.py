from apis import db, api
from flask_restx import fields
from apis.data_models.base import BaseMode

region_params = api.model(
    'Region',
    {
        'id': fields.Integer(),
        'region': fields.String(required=False),
        'recovered': fields.Integer(required=True),
        'deaths': fields.Integer(required=True),
        'confirmed': fields.Integer(required=True),
        'country_id': fields.Integer(),
        'lat': fields.String(required=False),
        'long': fields.String(required=False),
        'updated': fields.String(required=False)
    }
)


class RegionModel(BaseMode, db.Model):
    __tablename__ = 'region'
    id = db.Column(db.Integer(), primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    region = db.Column(db.String(200), nullable=True)
    recovered = db.Column(db.BigInteger(), nullable=True)
    confirmed = db.Column(db.BigInteger(), nullable=True)
    deaths = db.Column(db.BigInteger(), nullable=True)
    lat = db.Column(db.String(80), nullable=True)
    long = db.Column(db.String(80), nullable=True)
    updated = db.Column(db.String(80), nullable=True)
    db.UniqueConstraint(country_id, region)
