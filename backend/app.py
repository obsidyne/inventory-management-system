from flask import Flask , request
from supabase import create_client
from flask_cors import CORS
import mysql.connector  as connector


def connect():
    print("connecting to db")
    
    try:
        connection = connector.connect(
                host="127.0.0.1",
                user="root",
                password="8411",
                database="inventory_management_system",
                port=3306

            )


        print("connected to db")
        cursor = connection.cursor()
    

        return connection , cursor 

    except Exception as e:
        print("the error is", e)

    




app = Flask(__name__)

@app.route("/")
def home():
    return "its working"


@app.route("/add_customer", methods = ["POST"])
def add_customer():

    data = request.json 

    customer_name = data.get("customer_name")
    customer_email = data.get("customer_email")
    customer_phone =  data.get("customer_phone")
    customer_address = data.get("customer_address")

    data_to_insert = {
        "customer_name": customer_name , 
        "customer_phone": customer_phone , 
        "customer_email"  : customer_email , 
        "customer_adress" : customer_address  
    }



@app.route("/add_product", methods = ["POST"])
def add_product():
    data = request.json 

    product_name = data.get("product_name")
    product_brand = data.get("product_brand")
    product_manufacturing_date = data.get("product_manufacturing_date")
    buying_price = data.get("buying_price")
    selling_price = data.get("selling_price")
    quantity = 0 

    data_to_insert = {
        "product_name": product_name ,
        "product_brand ":product_brand ,
        "product_manufacturing_date":product_manufacturing_date,
        "buying_price":buying_price,
        "selling_price":selling_price,
        "quantity":quantity
    }


@app.route("/add_brand",methods = ["POST"])
def add_brand():
    data=request.json


    print("entered function")
    print(data)

    brand_name = data.get("brand_name")
    brand_email = data.get("brand_email")
    brand_phone =  data.get("brand_phone")
    brand_address = data.get("brand_address")

    connection , cursor = connect()

    query = f"insert into brand values( default , '{brand_name}', '{brand_address}', '{brand_email}'  ,'{brand_phone}' )"

    cursor.execute(query)
    connection.commit()

    return "", 200


    

@app.route("/add_offer",methods = ["POST"])
def add_offers():
    data = request.json

    offer_id = data.get("offer_id")
    offer_product = data.get("offer_products")
    offer_valid_till = data.get("offer_valid_till")
    offer_starts_on = data.get("offers_starts_on")
    offer_percentage = data.get("offer_percentage")

    data_to_insert = {
    "offer_id ": offer_id ,
    "offer_product":offer_product,
    "offer_valid_till":offer_valid_till,
    "offer_starts_on":offer_starts_on,
    "offer_percentage":offer_percentage
    }



@app.route("/add_sales",methods = ["POST"])
def add_sales():
    data = request.json

    sale_customer = data.get("sale_customer")
    sale_product = data.get("sale_product")
    sale_date = data.get("sale_product")
    sale_quantity = data.get("sale_quantity")

    data_to_insert = {
        "sale_customer":sale_customer,
        "sale_product":sale_product,
        "sale_date":sale_date,
        "sale_quantity":sale_quantity
    }





app.run(debug=True)