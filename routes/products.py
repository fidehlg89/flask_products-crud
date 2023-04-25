from flask import Blueprint, jsonify, request

from models.products import all_products, create_product, get_single_product, \
                             update_single_product, delete_single_product

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        products_list = all_products()
        return jsonify(products_list)
    elif request.method == "POST":
        data = request.get_json()
        product = create_product(data)
        return jsonify(product)

@products_blueprint.route("/products/<product_id>", methods=["GET", "PUT", "DELETE"])
def single_product(product_id):
    if request.method == "GET":
        product = get_single_product(product_id)
        if product:
            return jsonify(product)
        else:
            return jsonify({"message": "Product not found"}), 404
    elif request.method == "PUT":
        data = request.get_json()
        product = update_single_product(product_id, data)
        return jsonify(product)
    elif request.method == "DELETE":
        delete_single_product(product_id)
        return jsonify({"message": "Product deleted"})