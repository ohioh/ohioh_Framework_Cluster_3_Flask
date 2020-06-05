import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class LocationLatSchema(Schema):
    latitude = ms_fields.Float()
    departure = ms_fields.Bool()
    class Meta:
        unknown = EXCLUDE


