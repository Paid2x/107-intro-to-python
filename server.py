from flask import Flask
from data import me, catalog
import json  
from flask_cors import CORS

api = Flask("store")
CORS(api) #This disables cors policy (sending requests to third party domains)


@api.get("/")
def root():
    return "Welcome to the API"

@api.get("/home")
def home():
    return "Hello I'm an API"

@api.get("/about")
def about():
    return json.dumps(me)

@api.get("/api/test")
def test():
    return "api is working" 


@api.get("/api/products")
def get_products():
    return json.dumps(catalog)   # will parse the [] to json

#/about shows your name 


# start the api/server
api.run(debug=True)