from datetime import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class LocationLatSchema(Schema):
    user_id = ms_fields.Str(required=True)
    user_timestamp = ms_fields.DateTime(default=datetime.now())
    location_id = ms_fields.Str(required=False)
    latitude = ms_fields.Float(required=False)
    departure = ms_fields.Bool(required=False)
    accuracy = ms_fields.Float(required=False)

    class Meta:
        unknown = EXCLUDE



