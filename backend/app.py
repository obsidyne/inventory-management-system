from flask import Flask 
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return "its working"


@app.route("/add_customer")
def add_customer():

    data = requests.json 

    customer_name = data.get("customer_name")
    customer_email = data.get("customer_email")
    customer_phone =  data.get("customer_phone")
    customer_address = data.get("customer_address")

app.run(debug=True)