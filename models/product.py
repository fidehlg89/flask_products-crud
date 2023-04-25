import uuid

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


def remove_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            PRODUCTS.remove(product)
            return True
    return False


def create_product(data):
    product = {
        "id": uuid.uuid4().hex,
        "name": data.get("name"),
        "desc": data.get("desc"),
        "price": data.get("price"),
        "quantity": data.get("quantity"),
        "available": data.get("available"),
    }
    PRODUCTS.append(product)
    return product


def get_all_products():
    return PRODUCTS


def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def update_product(product_id, data):
    remove_product(product_id)
    product = {
        "id": product_id,
        "name": data.get("name"),
        "price": data.get("price"),
        "desc": data.get("desc"),
        "quantity": data.get("quantity"),
        "available": data.get("available"),
    }
    PRODUCTS.append(product)
    return product


def delete_product(product_id):
    remove_product(product_id)


# routes
def all_products():
    return get_all_products()


def create_product(data):
    return create_product(data)


def get_single_product(product_id):
    return get_product(product_id)


def update_single_product(product_id, data):
    return update_product(product_id, data)


def delete_single_product(product_id):
    return delete_product(product_id)
