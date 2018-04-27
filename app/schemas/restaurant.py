from ..extensions import marshmallow
from marshmallow import fields


class RestaurantSchema(marshmallow.Schema):
    class Meta:
        fields = (
            'id',
            'acceptsReservations',
            'paymentAccepted',
            'openingHours',
            'address',
            'email',
            'foundingDate',
            'faxNumber',
            'name',
            'hasMenu',
            'servesCuisine', 
            'currenciesAccepted', 
            'priceRange', 
            'user_id'
        ) 