import uuid
from flask import Flask, request, abort
from flask_smorest import Api
from resources.item import blp as ItemBluePrint
from resources.store import blp as StoreBluePrint

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBluePrint)
api.register_blueprint(StoreBluePrint)

#
# @app.get("/store")
# def get_stores():
#     return {"stores": stores.values()}
#
#
# @app.post("/store")
# def create_store():
#     stores_data = request.get_json()
#
#     if ("name" not in stores_data):
#         abort(404, description="Bad request. Ensure 'name' is included in the JSON payload")
#
#     for store in stores:
#         if stores_data["name"] == store["name"]:
#             abort(404, description="Store already exists")
#
#     store_id = uuid.uuid4().hex
#     new_store = {**stores_data, "id": store_id}
#     stores[store_id] = new_store
#     return new_store, 201
#
#
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if ("price" not in item_data or "name" not in item_data or "store_id" not in item_data):
#         abort(404, description="Bad request. Ensure 'price', 'store_id', and 'name' are include in the JSON payload")
#
#     for item in items.values():
#         if (item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
#             abort(404, description=f"{item_data.name} already exists!!!")
#
#     if item_data["store_id"] not in stores:
#         abort(404, description="Store not found")
#     item_id = uuid.uuid4().hex
#     new_item = {**item_data, "id": item_id}
#     items[item_id] = new_item
#     return new_item, 201
#
#
# @app.get("/item/<string:name>")
# def get_item(name):
#     if name not in items:
#         abort(404, description="Store not found")
#     return items[name]
#
#
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}
#
#
# @app.get("/stores")
# def get_all_stores():
#     return {"stores": list(stores.values())}
#
#
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted"}
#     except KeyError:
#         abort(404, descripion="Item not found")
#
#
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(404, description="Bad request. Please ensure that 'price' and 'name' are included in the JSON payload")
#
#     try:
#         item_to_update = items[item_id]
#         item_to_update |= item_data
#     except KeyError:
#         abort(404, description="Item not found")
#
#
# @app.delete("/store/<string:store_id>")
# def delete_item(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted"}
#     except KeyError:
#         abort(404, descripion="Store not found")
#
#
# if __name__ == '__main__':
#     app.run()
