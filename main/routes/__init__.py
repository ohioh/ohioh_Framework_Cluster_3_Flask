from flask import Blueprint
from .location_lat import LocationLatList, LocationLat
from flask_restful import Api

from .beat import Beat

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/ohioh/api/v1')

api.add_resource(Beat, '/')
api.add_resource(LocationLatList, '/location-lat')
api.add_resource(LocationLat, '/location-lat/<location_id>')
