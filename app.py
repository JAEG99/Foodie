from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from env.py
load_dotenv()

app = Flask(__name__)

mongo_connection_string = os.getenv("MONGO_CONNECTION_STRING")
database_name = os.getenv("Cluster0")

client = MongoClient(mongo_connection_string)
database = client["Recipe"]
recipe_collection = database["Recipe"]

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