from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)




@app.route('/recipe_form')
def recipe_form():
    return render_template('recipe_input.html')

# Create a route to handle form submission
@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    if request.method == 'POST':
        name = request.form.get('name')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        prep_time = request.form.get('prep_time')
        cook_time = request.form.get('cook_time')
        servings = request.form.get('servings')

        # Store the recipe in MongoDB
        recipe_data = {
            'name': name,
            'ingredients': ingredients,
            'instructions': instructions,
            'prep_time': prep_time,
            'cook_time': cook_time,
            'servings': servings
        }

        collection.insert_one(recipe_data)

        
@app.route('/success')
def success_page():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)