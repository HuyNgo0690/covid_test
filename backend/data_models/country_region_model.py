from __main__ import db


class CountryRegionModel(db.Model):
    __tablename__ = 'country_region'
    id = db.Column(db.Integer(), primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    db.UniqueConstraint(country_id, region_id)
