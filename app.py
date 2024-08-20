import uuid
from flask import Flask, request
from db import stores, items

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": stores.values()}


@app.post("/store")
def create_store():
    stores_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**stores_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.get("/item/<string:name>")
def get_item(name):
    if name not in items:
        return {"message": "Store not found"}, 404
    return items[name]

if __name__ == '__main__':
    app.run()
