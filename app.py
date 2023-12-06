import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

port = int(os.environ.get("PORT", 5000))

mongo = PyMongo(app)


@app.route('/')
def index():
    # Fetch a random recipe from MongoDB
    random_recipe = mongo.db.Foodie.aggregate([{ '$sample': { 'size': 1 } }]).next()

    # Render the template with the random recipe
    return render_template('index.html', random_recipe=random_recipe)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    # Hash the password before storing it
    hashed_password = generate_password_hash(password, method='sha256')

    # Save the user to the database
    user_data = {"USER": username, "PASSWORD": hashed_password}
    mongo.db.Users.insert_one(user_data)

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Retrieve the user from the database
    user_data = mongo.db.Users.find_one({'USER': username})

    if user_data and check_password_hash(user_data['PASSWORD'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

app.route("/recipe_form")
def recipe_form():
    return render_template("recipe_form.html")

@app.route("/submit_recipe", methods=["POST"])
def submit_recipe():
    
    recipe_name = request.form.get("name")
    ingredients = request.form.get("ingredients").split(",")  
    instructions = request.form.get("instructions")
    prep_time = int(request.form.get("prep_time"))
    cook_time = int(request.form.get("cook_time"))
    servings = int(request.form.get("servings"))

    
    insert_into_ingredients(recipe_name, ingredients)
    insert_into_recipe(recipe_name, instructions, prep_time, cook_time, servings)
    insert_into_reviews(recipe_name)

    return redirect(url_for("index"))

def insert_into_ingredients(recipe_name, ingredients):
    ingredients_data = {"recipe_name": recipe_name, "ingredients": ingredients}
    mongo.db.Ingredients.insert_one(ingredients_data)

def insert_into_recipe(recipe_name, instructions, prep_time, cook_time, servings):
    recipe_data = {
        "recipe_name": recipe_name,
        "instructions": instructions,
        "prep_time": prep_time,
        "cook_time": cook_time,
        "servings": servings
    }
    mongo.db.Recipe.insert_one(recipe_data)

def insert_into_reviews(recipe_name):
    
    review_data = {
        "recipe_name": recipe_name,
        "review_text": "Placeholder review text",
        "star_rating": 4
    }
    db.Reviews.insert_one(review_data)



if __name__ == "__main__":
    app.run(debug=False)