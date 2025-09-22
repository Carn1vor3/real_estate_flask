from flask import Blueprint, jsonify

from app.models import Listing
from app.schemas.listings import ListingsListSchema

listings_bp = Blueprint("listings", __name__, url_prefix="/listings")

@listings_bp.get("/")
def list_listings():
    schema = ListingsListSchema(many=True)
    listings = Listing.query.all()
    result = schema.dump(listings)
    return jsonify(result)