import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "All_recipies"
app.config["MONGO_URI"] = "mongodb+srv://ChefsBook:Recipies2019@recipebook-ksofe.mongodb.net/All_recipies?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')

#Go to Home Page
@app.route('/home_page')
def home_page():
    return render_template('index.html')


#View Recipes
@app.route('/all_recipes')
def all_recipes():
    return render_template('all_recipes.html', recipes=mongo.db.recipes.find())

    
#Search Recipe term
@app.route('/search_bar/', methods=['POST'])
def search_bar():
    search_term = request.form['search_text']
    if (search_term != ''):
        return redirect(url_for('search_results', search_text=search_term))
    else:
        return render_template('all_recipes.html', recipes=mongo.db.recipes.find())

#Search route
@app.route('/search_results<search_text>')
def search_results(search_text):
    mongo.db.recipes.create_index([("$**", 'text')])
    search_results = mongo.db.recipes.find({'$text': {'$search': search_text}})
    return render_template('search_result.html', recipes=search_results)
   


#Display single recipe
@app.route('/single_recipe/<recipe_id>')
def single_recipe(recipe_id):
    return render_template('single_recipe.html', recipes=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))


    
#Add Recipe Form 
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
    Categories=mongo.db.Categories.find(), 
    difficulty=mongo.db.difficulty.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    
    recipe_name = request.form['recipe_name']
    recipe_description = request.form['recipe_description']
    dish_type = request.form['dish_type']
    recipe_difficulty = request.form['recipe_difficulty']
    recipe_serving = request.form['recipe_serving']
    preparation_time = request.form['preparation_time']
    cooking_time = request.form['cooking_time']
    recipe_ingredients = request.form.getlist('recipe_ingredients')
    recipe_instruction = request.form.getlist('recipe_instruction')
    
    recipe_form = {
        "recipe_name" : recipe_name,
        "recipe_description" : recipe_description,
        "dish_type" : dish_type,
        "recipe_serving" : recipe_serving,
        "recipe_difficulty" : recipe_difficulty,
        "preparation_time" : preparation_time,
        "cooking_time" : cooking_time,
        "recipe_ingredients" : recipe_ingredients,
        "recipe_instruction" : recipe_instruction,
    }
    
    recipes.insert_one(recipe_form)
    return redirect(url_for('all_recipes'))



#Edit Recipe Form
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    all_categories = mongo.db.Categories.find()
    the_level = mongo.db.difficulty.find()
    return render_template('edit_recipe.html', recipe=the_recipe, Categories=all_categories, difficulty=the_level)


#Submit Change of a Recipe
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name' : request.form.get('recipe_name'),
        'recipe_description' : request.form.get('recipe_description'),
        'dish_type' : request.form.get('dish_type'),
        'recipe_difficulty' : request.form.get('recipe_difficulty'),
        'recipe_serving' : request.form.get('recipe_serving'),
        'preparation_time' : request.form.get('preparation_time'),
        'cooking_time' : request.form.get('cooking_time'),
        'recipe_ingredients' : request.form.getlist('recipe_ingredients'),
        'recipe_instruction' : request.form.getlist('recipe_instruction')
    })
    
    return redirect(url_for('single_recipe', recipe_id=recipe_id ))


#Delete Recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('home_page'))


    
if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")),
            debug=True)