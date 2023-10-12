from app.models import Role
from marshmallow import validate, fields, Schema, post_load

class RoleSchema(Schema):
    id = fields.Int(dump_only=True) #no pide id para crear un rol y lo devuelve solo cdo se pide
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    data = fields.Nested('RoleDataSchema')

    @post_load
    def make_role(self, data, **kwargs): #este método permite convertir a objeto Role
        return Role(**data)
