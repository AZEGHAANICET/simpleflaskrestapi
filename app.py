from flask import Flask

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
    return {"stores":stores}

if __name__ == '__main__':
    app.run()
