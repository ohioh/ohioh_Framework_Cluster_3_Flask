import json
from flask import request
from main import mongo
from flask_restful import Resource
from ..schemas.location_lat import LocationLatSchema
from ..services.db import DbOperations


location_lat = mongo.ohioh.location_lat
db = DbOperations(collections=location_lat, schema=LocationLatSchema)


class LocationLatList(Resource):
    def get(self):
        return db.find_all()

    def post(self):
        payload = request.get_json()
        return db.insert(payload)


class LocationLat(Resource):
    def get(self, location_id):
        return db.find_one(
            criteria={'location_id': location_id}
        )

    def put(self, location_id):
        payload = request.get_json()
        return db.update(
            criteria={'location_id': location_id},
            updated_value=payload
        )

    def delete(self, location_id):
        return db.delete(
            criteria={'location_id': location_id}
        )
