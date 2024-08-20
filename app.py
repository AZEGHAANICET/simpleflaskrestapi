from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 150
            }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data["name"], "items":[]}




if __name__ == '__main__':
    app.run()
