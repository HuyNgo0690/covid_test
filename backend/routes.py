from data_models.country_model import CountryModel
from data_models.country_region_model import CountryRegionModel
from data_models.region_model import RegionModel
from apis.region_api import Regions
from apis.country_api import Countries, CountryResource

api.add_resource(Regions, "/country/<int:country_id>/region")
api.add_resource(Countries, "/country")
api.add_resource(CountryResource, "/country/<int:_id>")