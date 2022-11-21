from sqlalchemy.orm import relationship

from backend import db
from backend.entities.country import Country


class User(db.Model):
    __tablename__ = "backend_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    country_id = db.Column(db.Integer, db.ForeignKey(Country.id))
    country = relationship(Country.__name__)
    profile = relationship("Profile", userlist=False, back_populates="user")

    class Profile(db.Model):
        __tablename__ = "profile"

        id = db.Column(db.Integer, primary_key=True)
        birth_date = db.Column(db.DateTime)
        job = db.Column(db.String(100))
        user_id = db.Column(db.Integer, db.ForeignKey(User.id))
        user = relationship(User.__name__, userlist=False, back_populates="profile")