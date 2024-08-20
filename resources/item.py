import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        if item_id not in items:
            abort(404, description="item not found")
        return items[item_id]


    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "item deleted"}
        except KeyError:
            abort(404, descripion="item not found")
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        if "price" not in item_data or "name" not in item_data:
            abort(404, description="Bad request. Please ensure that 'price' and 'name' are included in the JSON payload")

        try:
            item_to_update = items[item_id]
            item_to_update |= item_data
        except KeyError:
            abort(404, description="Item not found")
        return item_to_update


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        for item in items.values():
            if (item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
                abort(404, description=f"{item_data.name} already exists!!!")

        if item_data["store_id"] not in stores:
            abort(404, description="Store not found")
        item_id = uuid.uuid4().hex
        new_item = {**item_data, "id": item_id}
        items[item_id] = new_item
        return new_item, 201
