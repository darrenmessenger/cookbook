import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.secret_key = 'randomstring123'

MONGODB_URI = os.getenv("MONGO_URI")
print("Mongo is connected!")
print(MONGODB_URI)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template("index.html", username=session['username'],
                           recipes=mongo.db.recipes.find())
    return render_template("index.html", username='',
                           recipes=mongo.db.recipes.find())
                           
@app.route('/logout')
def logout():
    session['username'] = ''
    return redirect(url_for('index'))

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
            
@app.route('/edit_recipe/<recipe_id>', methods = ['GET','POST'])
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html',
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))
    
@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    return render_template('display_recipe.html',
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))
    
@app.route('/update_recipe/<recipe_id>', methods = ['GET','POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_method': request.form.get('recipe_method'),
        'recipe_author': request.form.get('recipe_author'),
        'recipe_image_url': request.form.get('recipe_image_url')
    })
    return redirect(url_for('index'))
    
@app.route('/delete_recipe/<recipe_id>', methods = ['GET','POST'])
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))
  
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        
        if not login_user:
            flash('Incorrect username')  
    
        if login_user:
            
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                flash('You have been successfully logged in')  
                return render_template("index.html", username=session['username'],
                           recipes=mongo.db.recipes.find())
     
            flash('Incorrect password')  
    return render_template('login.html')

                       
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        flash('That username already exists!')  
        
    return render_template('register.html')
    
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)