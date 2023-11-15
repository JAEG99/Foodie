from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging
import sys

# Load environment variables
if os.path.exists("env.py"):
    import env
load_dotenv()

# Set up Flask app
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Attempt to connect to MongoDB and log relevant information
mongo = PyMongo(app)
logging.debug(f"MongoDB URI: {app.config['MONGO_URI']}")
try:
    mongo.init_app(app)
    logging.debug("Connected to MongoDB")
except Exception as e:
    logging.error(f"Failed to connect to MongoDB: {e}")

logging.debug(f"MongoDB database: {mongo.db}")

# Your routes and other code go here

if __name__ == '__main__':
    app.run(debug=True)
