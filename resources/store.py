import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        if store_id not in stores:
            abort(404, description="Store not found")
        return stores[store_id]

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(404, descripion="Store not found")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, stores_data):
        if "name" not in stores_data:
            abort(404, description="Bad request. Ensure 'name' is included in the JSON payload")

        for store in stores:
            if stores_data["name"] == store["name"]:
                abort(404, description="Store already exists")

        store_id = uuid.uuid4().hex
        new_store = {**stores_data, "id": store_id}
        stores[store_id] = new_store
        return new_store, 201
