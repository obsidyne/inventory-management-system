from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(_name_)

# Configure database connection
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Renjith@1234',
    'database': 'inventory_management_system'
}

# Establish a connection to the MySQL database
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Endpoint to create a new customer
@app.route('/create_customer', methods=['POST'])
def create_customer():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customers (customer_name, customer_phone, customer_email, customer_address) VALUES (%s, %s, %s, %s)",
            (data['customer_name'], data['customer_phone'], data['customer_email'], data['customer_address'])
        )
        conn.commit()
        return jsonify({"message": "Customer created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Endpoint to create a new product
@app.route('/create_product', methods=['POST'])
def create_product():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO product (product_name, product_brand, product_manufacturing_date, buying_price, product_desc, selling_price, weight, product_quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (data['product_name'], data['product_brand'], data['product_manufacturing_date'], data['buying_price'], data['product_desc'], data['selling_price'], data['weight'], data['product_quantity'])
        )
        conn.commit()
        return jsonify({"message": "Product created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Endpoint to create a new brand
@app.route('/create_brand', methods=['POST'])
def create_brand():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO brand (brand_name) VALUES (%s)",
            (data['brand_name'],)
        )
        conn.commit()
        return jsonify({"message": "Brand created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Endpoint to create a new offer
@app.route('/create_offer', methods=['POST'])
def create_offer():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO offers (offer_product, offer_valid_till, offer_starts_on, offer_percentage) VALUES (%s, %s, %s, %s)",
            (data['offer_product'], data['offer_valid_till'], data['offer_starts_on'], data['offer_percentage'])
        )
        conn.commit()
        return jsonify({"message": "Offer created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Endpoint to create a new sale
@app.route('/create_sale', methods=['POST'])
def create_sale():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sales (sale_customer, sale_product, sale_date, sale_quantity, sale_status) VALUES (%s, %s, %s, %s, %s)",
            (data['sale_customer'], data['sale_product'], data['sale_date'], data['sale_quantity'], data['sale_status'])
        )
        conn.commit()
        return jsonify({"message": "Sale created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()



# Establish a connection to the MySQL database
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Endpoint to retrieve all brands
@app.route('/get_brands', methods=['GET'])
def get_brands():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM brand")
        brands = cursor.fetchall()
        return jsonify(brands), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint to retrieve all customers
@app.route('/get_customers', methods=['GET'])
def get_customers():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        return jsonify(customers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint to retrieve all sales
@app.route('/get_sales', methods=['GET'])
def get_sales():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sales")
        sales = cursor.fetchall()
        return jsonify(sales), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint to retrieve all offers
@app.route('/get_offers', methods=['GET'])
def get_offers():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM offers")
        offers = cursor.fetchall()
        return jsonify(offers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint to retrieve all products
@app.route('/get_products', methods=['GET'])
def get_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if _name_ == '_main_':
    app.run(debug=True)