import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
import sys

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
                           recipes=mongo.db.recipes.find(),courses=mongo.db.courses.find(),authors=mongo.db.authors.find(),course=None,author=None)
    return render_template("index.html", username='',
                           recipes=mongo.db.recipes.find(),courses=mongo.db.courses.find(),authors=mongo.db.authors.find(),course=None,author=None)
                           
@app.route('/logout')
def logout():
    session['username'] = ''
    return redirect(url_for('index'))

@app.route('/courses')
def courses():
    return render_template("courses.html",
                            courses=mongo.db.courses.find())

@app.route('/authors')
def authors():
    return render_template("authors.html",
                            authors=mongo.db.authors.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           authors=mongo.db.authors.find())

@app.route('/add_recipe', methods = ['GET','POST'])
def insert_recipe():
        if request.method == 'POST':
            recipe ={'recipe_name': request.form.get('recipe_name'),
                'recipe_description': request.form.get('recipe_description'),
                'recipe_ingredients': request.form.get('recipe_ingredients'),
                'recipe_method': request.form.get('recipe_method'),
                'recipe_course': request.form.get('recipe_course'),
                'recipe_author': request.form.get('recipe_author'),
                'recipe_image_url': request.form.get('recipe_image_url')
            }
           
            mongo.db.recipes.insert_one(recipe)

            return redirect(url_for('index'))
            

@app.route('/edit_recipe/<recipe_id>', methods = ['GET','POST'])
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html',
    recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}),
    courses=mongo.db.courses.find(),
    authors=mongo.db.authors.find())
    
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
        'recipe_course': request.form.get('recipe_course'),
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
                           recipes=mongo.db.recipes.find(),courses=mongo.db.courses.find(),authors=mongo.db.authors.find(),course=None,author=None)

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
    
@app.route('/recipe_filtered', methods = ['POST'])
def recipe_filtered():
    recipes=mongo.db.recipes
    course = request.form.get('course_name')
    author = request.form.get('author_name')
    title_search = request.form.get('title_search')

    if title_search is not None:
        recipes=mongo.db.recipes.find({"recipe_name": { "$regex": title_search}})
    if course is not None and author is not None:
        recipes=mongo.db.recipes.find({'recipe_course': course,'recipe_author': author})
    elif course is not None:
        recipes=mongo.db.recipes.find({'recipe_course': course})  
    elif author is not None:
        recipes=mongo.db.recipes.find({'recipe_author': author}) 
    else:
        recipes=mongo.db.recipes.find()
    
    
    if 'username' in session:
        return render_template("index.html", username=session['username'],
                           recipes=recipes,courses=mongo.db.courses.find(),authors=mongo.db.authors.find(),course=course,author=author)
    return render_template("index.html", username='',
                           recipes=recipes,courses=mongo.db.courses.find(),authors=mongo.db.authors.find(),course=course,author=author)
                         
@app.route('/get_courses')
def get_courses():
    return render_template('courses.html',
                           courses=mongo.db.courses.find())

@app.route('/delete_course/<course_id>', methods=["POST"])
def delete_course(course_id):
    mongo.db.courses.remove({'_id': ObjectId(course_id)})
    return redirect(url_for('get_courses'))

@app.route('/edit_course/<course_id>')
def edit_course(course_id):
    return render_template('edit_course.html',
    course=mongo.db.courses.find_one({'_id': ObjectId(course_id)}))


@app.route('/update_course/<course_id>', methods=['POST'])
def update_course(course_id):
    course = mongo.db.courses
    course.update( {'_id': ObjectId(course_id)},
    {
        'course_name': request.form.get('course_name')
    })
    return redirect(url_for('get_courses'))

@app.route('/insert_course', methods=['POST'])
def insert_course():
    course_doc = {'course_name': request.form.get('course_name')}
    mongo.db.courses.insert_one(course_doc)
    return redirect(url_for('get_courses'))

@app.route('/add_course')
def add_course():
    return render_template('add_course.html')
    
@app.route('/get_authors')
def get_authors():
    return render_template('authors.html',
                           authors=mongo.db.authors.find())

@app.route('/delete_authors/<author_id>', methods=["POST"])
def delete_author(author_id):
    mongo.db.authors.remove({'_id': ObjectId(author_id)})
    return redirect(url_for('get_authors'))

@app.route('/edit_author/<author_id>')
def edit_author(author_id):
    return render_template('edit_author.html',
    author=mongo.db.authors.find_one({'_id': ObjectId(author_id)}))


@app.route('/update_author/<author_id>', methods=['POST'])
def update_author(author_id):
    author = mongo.db.authors
    author.update( {'_id': ObjectId(author_id)},
    {
        'author_name': request.form.get('author_name')
    })
    return redirect(url_for('get_authors'))

@app.route('/insert_author', methods=['POST'])
def insert_author():
    author_doc = {'author_name': request.form.get('author_name')}
    mongo.db.authors.insert_one(author_doc)
    return redirect(url_for('get_authors'))

@app.route('/add_author')
def add_author():
    return render_template('add_author.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)