import re

from marshmallow import Schema, fields, validates, ValidationError, post_load

from backend.models.user import User


class UserCreationSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)

    @validates("password")
    def validates_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password length must be longer than 8")
        if not any(c.isupper() for c in value):
            raise ValidationError("Password must contain upper case")
        if not any(c.islower() for c in value):
            raise ValidationError("Password must contain lower case")

    @validates("email")
    def validates_email(self, value):
        if not re.match("[^^]+@[^@]+\.[^@]+", value):
            raise ValidationError("invalid email format")

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
