import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "All_recipies"
app.config["MONGO_URI"] = "mongodb+srv://ChefsBook:Recipies2019@recipebook-ksofe.mongodb.net/All_recipies?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")

#Go to Home Page
@app.route("/home-page")
def home_page():
    return render_template("index.html")

#Get all recipes
@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)