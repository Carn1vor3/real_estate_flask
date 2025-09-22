from marshmallow import Schema, fields


class ListingsListSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    price = fields.Float()
    area = fields.Float()
    floor = fields.Int()
    city = fields.Str()
    address = fields.Str()
    created_at = fields.DateTime()
