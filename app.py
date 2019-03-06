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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)