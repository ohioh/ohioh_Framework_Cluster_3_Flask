import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class LocationLatSchema(Schema):
    locationID = ms_fields.Str()
    latitude = ms_fields.Int()
    departure = ms_fields.Bool()
    class Meta:
        unknown = EXCLUDE

