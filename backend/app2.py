from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_management_system"]

# Access collections (tables)
customers = db["customers"]
brands = db["brands"]
products = db["products"]
sales = db["sales"]
invoices = db["invoices"]


# Helper function to serialize MongoDB ObjectId to string
def serialize_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj


# Endpoint to add a customer
@app.route("/add_customer", methods=["POST"])
def add_customer():
    data = request.get_json()
    customer = {
        "customer_name": data["customer_name"],
        "customer_email": data["customer_email"],
        "customer_phone": data["customer_phone"],
        "customer_address": data["customer_address"],
    }
    result = customers.insert_one(customer)
    return jsonify({"message": "Customer added", "customer_id": str(result.inserted_id)})


# Endpoint to add a brand
@app.route("/brands", methods=["POST"])
def add_brand():
    data = request.get_json()
    brand = {
        "brand_name": data["brand_name"],
        "brand_address": data["brand_address"],
        "brand_email": data["brand_email"],
        "brand_phone": data["brand_phone"],
    }
    result = brands.insert_one(brand)
    return jsonify({"message": "Brand added", "brand_id": str(result.inserted_id)})


# Endpoint to add an invoice (along with sales)
@app.route("/invoices", methods=["POST"])
def add_invoice():
    data = request.get_json()
    invoice = {
        "invoice_date": data["invoice_date"],
        "invoice_customer": ObjectId(data["invoice_customer"]),  # Customer ID
    }
    result_invoice = invoices.insert_one(invoice)

    # Add sales
    for sale in data["sales"]:
        sale_data = {
            "sale_product": ObjectId(sale["sale_product"]),  # Product ID
            "sale_quantity": sale["sale_quantity"],
        }
        sales.insert_one(sale_data)

    return jsonify({"message": "Invoice and sales added", "invoice_id": str(result_invoice.inserted_id)})


# Endpoint to delete a customer
@app.route("/customers/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    result = customers.delete_one({"_id": ObjectId(customer_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Customer deleted"})
    return jsonify({"message": "Customer not found"})


# Endpoint to delete a brand
@app.route("/brands/<brand_id>", methods=["DELETE"])
def delete_brand(brand_id):
    result = brands.delete_one({"_id": ObjectId(brand_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Brand deleted"})
    return jsonify({"message": "Brand not found"})


# Endpoint to delete an invoice
@app.route("/invoices/<invoice_id>", methods=["DELETE"])
def delete_invoice(invoice_id):
    result = invoices.delete_one({"_id": ObjectId(invoice_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Invoice deleted"})
    return jsonify({"message": "Invoice not found"})


# Endpoint to retrieve all customers
@app.route("/customers", methods=["GET"])
def get_all_customers():
    customers_list = [serialize_objectid(customer) for customer in customers.find()]
    return jsonify(customers_list)


# Endpoint to retrieve all brands
@app.route("/brands", methods=["GET"])
def get_all_brands():
    brands_list = [serialize_objectid(brand) for brand in brands.find()]
    return jsonify(brands_list)


# Endpoint to retrieve all products
@app.route("/products", methods=["GET"])
def get_all_products():
    products_list = [serialize_objectid(product) for product in products.find()]
    return jsonify(products_list)


# Endpoint to retrieve all invoices
@app.route("/invoices", methods=["GET"])
def get_all_invoices():
    invoices_list = [serialize_objectid(invoice) for invoice in invoices.find()]
    return jsonify(invoices_list)


# Endpoint to retrieve all sales
@app.route("/sales", methods=["GET"])
def get_all_sales():
    sales_list = [serialize_objectid(sale) for sale in sales.find()]
    return jsonify(sales_list)


# Endpoint to retrieve a single product
@app.route("/products/<product_id>", methods=["GET"])
def get_single_product(product_id):
    product = products.find_one({"_id": ObjectId(product_id)})
    if product:
        return jsonify(serialize_objectid(product))
    return jsonify({"message": "Product not found"})


# Endpoint to retrieve a single brand
@app.route("/brands/<brand_id>", methods=["GET"])
def get_single_brand(brand_id):
    brand = brands.find_one({"_id": ObjectId(brand_id)})
    if brand:
        return jsonify(serialize_objectid(brand))
    return jsonify({"message": "Brand not found"})


# Endpoint to retrieve a single invoice
@app.route("/invoices/<invoice_id>", methods=["GET"])
def get_single_invoice(invoice_id):
    invoice = invoices.find_one({"_id": ObjectId(invoice_id)})
    if invoice:
        return jsonify(serialize_objectid(invoice))
    return jsonify({"message": "Invoice not found"})


# Endpoint to retrieve a single sale
@app.route("/sales/<sale_id>", methods=["GET"])
def get_single_sale(sale_id):
    sale = sales.find_one({"_id": ObjectId(sale_id)})
    if sale:
        return jsonify(serialize_objectid(sale))
    return jsonify({"message": "Sale not found"})


# Endpoint to retrieve a single customer
@app.route("/customers/<customer_id>", methods=["GET"])
def get_single_customer(customer_id):
    customer = customers.find_one({"_id": ObjectId(customer_id)})
    if customer:
        return jsonify(serialize_objectid(customer))
    return jsonify({"message": "Customer not found"})


if __name__ == "__main__":
    app.run(debug=True)
