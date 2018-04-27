from ..extensions import marshmallow
from marshmallow import fields


class UserSchema(marshmallow.Schema):
    class Meta:
        fields = (
            'id', 
            'username', 
            'email', 
            'dob', 
            'name', 
            'telephone', 
            'address', 
            'gender'
        )
    