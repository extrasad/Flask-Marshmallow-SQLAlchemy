from ..database import db, Model , Column, relationship
from ..extensions import marshmallow

from sqlalchemy_utils import PasswordType, EmailType, ChoiceType, Timestamp, URLType
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates


from marshmallow import fields

import datetime, flask


class Restaurant(db.Model, Timestamp):

    __tablename__ = 'restaurant'
    id       = Column(db.Integer, primary_key=True)
    acceptsReservations = Column(db.Boolean)
    paymentAccepted = Column(db.String(80))
    openingHours = Column(db.String(80))
    address = Column(db.String(90))
    email    = Column(EmailType, unique=True)
    foundingDate = Column(db.Date)
    faxNumber = Column(db.String(20), unique=True)
    name = Column(db.String(90))
    hasMenu = Column(URLType)
    servesCuisine = Column(db.String(90))
    currenciesAccepted = Column(db.String(90))
    priceRange = Column(db.String(90))
    user_id = Column(db.Integer, db.ForeignKey('user.id'),
    nullable=False)