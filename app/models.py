from datetime import datetime
from .extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    listings = db.relationship("Listing", back_populates="user", cascade="all, delete-orphan")
    favorites = db.relationship("Favorite", back_populates="user", cascade="all, delete-orphan")


class Listing(db.Model):
    __tablename__ = "listings"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    area = db.Column(db.Float, nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="listings")

    favorites = db.relationship("Favorite", back_populates="listing", cascade="all, delete-orphan")


class Favorite(db.Model):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    listing_id = db.Column(db.Integer, db.ForeignKey("listings.id"))

    user = db.relationship("User", back_populates="favorites")
    listing = db.relationship("Listing", back_populates="favorites")
