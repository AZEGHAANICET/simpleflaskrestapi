import uuid
from flask import Flask, request, abort
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
    if("price" not in item_data or "name" not in item_data or "store_id" not in item_data):
        abort(404, description="Bad request. Ensure 'price', 'store_id', and 'name' are include in the JSON payload")

    for item in items.values():
        if(item_data["name"]==item["name"] and item_data["store_id"]==item["store_id"]):
            abort(404, description=f"{item_data.name} already exists!!!")

    if item_data["store_id"] not in stores:
        abort(404, description="Store not found")
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.get("/item/<string:name>")
def get_item(name):
    if name not in items:
        abort(404, description="Store not found")
    return items[name]


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message":"Item deleted"}
    except KeyError:
        abort(404, descripion="Item not found")




@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(404, description="Bad request. Please ensure that 'price' and 'name' are included in the JSON payload")

    try:
        item_to_update = items[item_id]
        item_to_update |=item_data
    except KeyError:
        abort(404, description="Item not found")

if __name__ == '__main__':
    app.run()
