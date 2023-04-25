from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

PRODUCTS = [
    {
        "id": uuid.uuid4().hex,
        "name": "Banana",
        "desc": "Monkey fruit",
        "price": "1.50",
        "quantity": "100",
        "available": True,
    },
    {
        "id": uuid.uuid4().hex,
        "name": "Apple",
        "desc": "Rich Apple",
        "price": "5.20",
        "quantity": "20",
        "available": False,
    },
    {
        "id": uuid.uuid4().hex,
        "name": "Watermelon",
        "desc": "Single fruit",
        "price": "2.50",
        "quantity": "80",
        "available": False,
    },
]


# sanity check route
@app.route("/products", methods=["GET", "POST"])
def all_products():
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        product = {
            "id": uuid.uuid4().hex,
            "name": post_data.get("name"),
            "desc": post_data.get("desc"),
            "price": post_data.get("price"),
            "quantity": post_data.get("quantity"),
            "available": post_data.get("available"),
        }
        PRODUCTS.append(product)
        response_object["message"] = "Product added!"
    else:
        response_object["products"] = PRODUCTS
    return jsonify(response_object)


@app.route("/products/<product_id>", methods=["PUT", "DELETE"])
def single_product(product_id):
    response_object = {"status": "success"}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_product(product_id)
        product = {
            "id": uuid.uuid4().hex,
            "name": post_data.get("name"),
            "price": post_data.get("price"),
            "desc": post_data.get("desc"),
            "quantity": post_data.get("quantity"),
            "available": post_data.get("available"),
        }
        PRODUCTS.append(product)
        response_object["message"] = "Product updated!"
    if request.method == "DELETE":
        remove_product(product_id)
        response_object["message"] = "Product removed!"
    return jsonify(response_object)


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


def remove_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            PRODUCTS.remove(product)
            return True
    return False


if __name__ == "__main__":
    app.run()
