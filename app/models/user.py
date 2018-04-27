from ..database import db, Model , Column, relationship
from ..extensions import marshmallow

from sqlalchemy_utils import PasswordType, EmailType, ChoiceType, Timestamp
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates


from marshmallow import fields

import datetime, flask


class User(db.Model, Timestamp):
    GENDER = [
    (u'Male', u'M'),
    (u'Female', u'F')
  ]
    __tablename__ = 'user'
    id       = Column(db.Integer, primary_key=True)
    username = Column(db.String(80), unique=True)
    name = Column(db.String(80))
    telephone = Column(db.String(15), unique=True)
    address = Column(db.String(90))
    gender = Column(ChoiceType(GENDER), nullable=False, default=u'Female' )
    email    = Column(EmailType)
    dob      = Column(db.Date)
    nationality = Column(db.String(90))
    password = Column(
        PasswordType(
            onload=lambda **kwargs: dict(
                schemes=flask.current_app.config['PASSWORD_SCHEMES'],
                **kwargs
            ),
        ),
        unique=False,
        nullable=False,
    )
    userRestaurants = db.relationship('Restaurant', backref='user')