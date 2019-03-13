import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGO_URI")
print("Mongo is connected!")
print(MONGODB_URI)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html", 
                           recipes=mongo.db.recipes.find())
    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/categories')
def categories():
    return render_template('categories.html')
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')
    
@app.route('/add_recipe', methods = ['GET','POST'])
def insert_recipe():
        if request.method == 'POST':
            recipe ={'recipe_name': request.form.get('recipe_name'),
                'recipe_description': request.form.get('recipe_description'),
                'recipe_ingredients': request.form.get('recipe_ingredients'),
                'recipe_method': request.form.get('recipe_method'),
                'recipe_author': request.form.get('recipe_author'),
                'recipe_image_url': request.form.get('recipe_image_url')
            }
           
            mongo.db.recipes.insert_one(recipe)

            return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)