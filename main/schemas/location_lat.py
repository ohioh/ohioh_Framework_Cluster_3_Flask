from datetime import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class LocationLatSchema(Schema):
    user_id = ms_fields.Str(required=True)
    user_timestamp = ms_fields.DateTime(default=datetime.now())
    location_id = ms_fields.Str(default="")
    latitude = ms_fields.Float(default=0.0)
    departure = ms_fields.Bool(default=False)
    accuracy = ms_fields.Float(default=0.0)

    class Meta:
        unknown = EXCLUDE



