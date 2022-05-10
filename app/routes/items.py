from flask import Blueprint, jsonify
from app.models import Item

item_routes = Blueprint('items',__name__, url_prefix="/items")

@item_routes.route('/')
def items():
    items = Item.query.all()
    return {'items': [item.to_dict() for item in items]}
