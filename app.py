from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os  

if os.path.exists("env.py"):
    import env

# Load environment variables from env.py
load_dotenv()

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
recipe_collection = mongo.db.Foodie  # Adjust this line

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        description = request.form['description']
        instructions = request.form['instructions']

        recipe_data = {
            "RECIPE_NAME": recipe_name,
            "RECIPE_description": description,
            "RECIPE_Instructions": instructions
        }

        recipe_collection.insert_one(recipe_data)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)