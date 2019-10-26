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
    
#Add Recipe Form 
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
    Categories=mongo.db.Categories.find(), 
    difficulty=mongo.db.difficulty.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('all-recipes.html'))





    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)