import json
from flask import request
from main import mongo
from flask_restful import Resource
from ..schemas.location_lat import LocationLatSchema
from ..services.db import DbOperations
from bson.objectid import ObjectId

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
            criteria={'_id': ObjectId(location_id)}
        )

    def put(self, location_id):
        payload = request.get_json()
        return db.update(
            criteria={'_id': ObjectId(location_id)},
            updated_value=payload
        )

    def delete(self, location_id):
        return db.delete(
            criteria={'_id': ObjectId(location_id)}
        )
