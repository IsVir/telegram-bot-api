from marshmallow import Schema, fields


class MaskPositionSchema(Schema):
    point = fields.Str(required=True, validate=lambda x: x in ['forehead', 'eyes', 'mouth', 'chin'])
    x_shift = fields.Float(required=True)
    y_shift = fields.Float(required=True)
    scale = fields.Float(required=True)
