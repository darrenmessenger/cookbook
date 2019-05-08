import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
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


""" Variables """
db_users = mongo.db.users
db_recipes = mongo.db.recipes
db_courses = mongo.db.courses
db_authors = mongo.db.authors


@app.route('/')
def index():
    """ Home Page """
    if 'username' in session:
        return render_template("index.html", username=session['username'],
                           recipes=db_recipes.find(),courses=db_courses.find(),authors=db_authors.find(),course=None,author=None,is_vegetarian=None)
    return render_template("index.html", username='',
                           recipes=db_recipes.find(),courses=db_courses.find(),authors=db_authors.find(),course=None,author=None)
 

@app.route('/logout')
def logout():
    """ Log out button pressed """
    session['username'] = ''
    return redirect(url_for('index'))


@app.route('/courses')
def courses():
    """ Manage the Courses page """
    return render_template("courses.html",
                            courses=db_courses.find())


@app.route('/authors')
def authors():
    """ Manage the Authors page """
    return render_template("authors.html",
                            authors=db_authors.find())


@app.route('/add_recipe')
def add_recipe():
    """ Add a recipe page """
    return render_template('add_recipe.html',
                           courses=db_courses.find(),
                           authors=db_authors.find())

@app.route('/add_recipe', methods = ['GET','POST'])
def insert_recipe():
        if request.method == 'POST':
            recipe ={'recipe_name': request.form.get('recipe_name'),
                'recipe_description': request.form.get('recipe_description'),
                'recipe_ingredients': request.form.get('recipe_ingredients'),
                'recipe_method': request.form.get('recipe_method'),
                'recipe_course': request.form.get('recipe_course'),
                'recipe_author': request.form.get('recipe_author'),
                'recipe_image_url': request.form.get('recipe_image_url'),
                'recipe_is_vegetarian':request.form.get('is_vegetarian'),
                'recipe_is_vegan':request.form.get('is_vegan'),
                'recipe_is_glutenfree':request.form.get('is_glutenfree'),
                'recipe_entered_by' :session['username']
            }
           
            db_recipes.insert_one(recipe)

            return redirect(url_for('index'))
            

@app.route('/edit_recipe/<recipe_id>', methods = ['GET','POST'])
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html',
    recipe=db_recipes.find_one({'_id': ObjectId(recipe_id)}),
    courses=db_courses.find(),
    authors=db_authors.find())
    
@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    return render_template('display_recipe.html', username=session['username'],
    recipe=db_recipes.find_one({'_id': ObjectId(recipe_id)}))
    
@app.route('/update_recipe/<recipe_id>', methods = ['GET','POST'])
def update_recipe(recipe_id):
    recipes = db_recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_method': request.form.get('recipe_method'),
        'recipe_course': request.form.get('recipe_course'),
        'recipe_author': request.form.get('recipe_author'),
        'recipe_image_url': request.form.get('recipe_image_url'),
        'recipe_is_vegetarian':request.form.get('is_vegetarian'),
        'recipe_is_vegan':request.form.get('is_vegan'),
        'recipe_is_glutenfree':request.form.get('is_glutenfree')
    })
    return redirect(url_for('index'))
    
@app.route('/delete_recipe/<recipe_id>', methods = ['GET','POST'])
def delete_recipe(recipe_id):
    db_recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))
  
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = db_users
        login_user = users.find_one({'name' : request.form['username']})
        
        if not login_user:
            flash('Incorrect username')  
    
        if login_user:
            
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                flash('You have been successfully logged in')  
                return render_template("index.html", username=session['username'],
                           recipes=db_recipes.find(),courses=db_courses.find(),authors=db_authors.find(),course=None,author=None)

            flash('Incorrect password')  
    return render_template('login.html')

                       
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = db_users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        flash('That username already exists!')  
        
    return render_template('register.html')
    
@app.route('/search')
def search():
    """ Route for the search"""
    query = request.args['query']
    recipes = db_recipes.find({'$text': {'$search': query }})
    if 'username' in session:
        return render_template("index.html", username=session['username'],
                               recipes=recipes,courses=db_courses.find(),authors=db_authors.find(),course=None,author=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)
    return render_template("index.html", username='',
                            recipes=recipes,courses=db_courses.find(),authors=db_authors.find(),course=None,author=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)

    
@app.route('/recipe_filtered', methods = ['POST'])
def recipe_filtered():
    if request.form.get('reset_button') == 'reset':
        print("Reset button pressed...")
        recipes=db_recipes.find()
        if 'username' in session:
            return render_template("index.html", username=session['username'],
                               recipes=recipes,courses=db_courses.find(),authors=db_authors.find(),course=None,author=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)
        return render_template("index.html", username='',
                               recipes=recipes,courses=db_courses.find(),authors=db_authors.find(),course=None,author=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)
                         
    else:
        print("recipe_filtered...")
        recipes=db_recipes
        course = request.form.get('course_name')
        author = request.form.get('author_name')
        vegetarian = request.form.get('is_vegetarian')
        vegan = request.form.get('is_vegan')
        glutenfree = request.form.get('is_glutenfree')
        
        filter_by = {}
        if vegetarian == "on":
            filter_by['recipe_is_vegetarian'] = 'on'
            print("filter_by: ",filter_by)
        if vegan == "on":
            filter_by['recipe_is_vegan'] = 'on'
            print("filter_by: ",filter_by)
        if glutenfree == "on":
            filter_by['recipe_is_glutenfree'] = 'on'
            print("filter_by: ",filter_by)
        if course is not None:
            filter_by['recipe_course'] = course
            print("filter_by: ",filter_by)
        if author is not None:
            filter_by['recipe_author'] = author
            print("filter_by: ",filter_by)
        print("filter_by type",type(filter_by))
        recipes=db_recipes.find({"$and":[ filter_by ]})
    
    
        if 'username' in session:
            return render_template("index.html", username=session['username'],
                               recipes=recipes,courses=db_courses.find(),authors=db_authors.find(),course=course,author=author,is_vegetarian=vegetarian,is_vegan=vegan,is_glutenfree=glutenfree)
        return render_template("index.html", username='',
                               recipes=recipes,courses=db_courses.find(),authors=db_authors.find(),course=course,author=author,is_vegetarian=vegetarian,is_vegan=vegan,is_glutenfree=glutenfree)
                         
@app.route('/get_courses')
def get_courses():
    return render_template('courses.html',
                           courses=db_courses.find())

@app.route('/delete_course/<course_id>', methods=["POST"])
def delete_course(course_id):
    db_courses.remove({'_id': ObjectId(course_id)})
    return redirect(url_for('get_courses'))

@app.route('/edit_course/<course_id>')
def edit_course(course_id):
    return render_template('edit_course.html',
    course=db_courses.find_one({'_id': ObjectId(course_id)}))


@app.route('/update_course/<course_id>', methods=['POST'])
def update_course(course_id):
    course = db_courses
    course.update( {'_id': ObjectId(course_id)},
    {
        'course_name': request.form.get('course_name')
    })
    return redirect(url_for('get_courses'))

@app.route('/insert_course', methods=['POST'])
def insert_course():
    course_doc = {'course_name': request.form.get('course_name')}
    db_courses.insert_one(course_doc)
    return redirect(url_for('get_courses'))

@app.route('/add_course')
def add_course():
    return render_template('add_course.html')
    
@app.route('/get_authors')
def get_authors():
    return render_template('authors.html',
                           authors=db_authors.find())

@app.route('/delete_authors/<author_id>', methods=["POST"])
def delete_author(author_id):
    db_authors.remove({'_id': ObjectId(author_id)})
    return redirect(url_for('get_authors'))

@app.route('/edit_author/<author_id>')
def edit_author(author_id):
    return render_template('edit_author.html',
    author=db_authors.find_one({'_id': ObjectId(author_id)}))


@app.route('/update_author/<author_id>', methods=['POST'])
def update_author(author_id):
    author = db_authors
    author.update( {'_id': ObjectId(author_id)},
    {
        'author_name': request.form.get('author_name')
    })
    return redirect(url_for('get_authors'))

@app.route('/insert_author', methods=['POST'])
def insert_author():
    author_doc = {'author_name': request.form.get('author_name')}
    db_authors.insert_one(author_doc)
    return redirect(url_for('get_authors'))

@app.route('/add_author')
def add_author():
    return render_template('add_author.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)