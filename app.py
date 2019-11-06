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
db_chefs = mongo.db.chefs


@app.route('/')
def index():
    """ Home Page """
    if 'username' in session:
        return render_template("index.html", username=session['username'],
                           recipes=db_recipes.find(),courses=db_courses.find(),chefs=db_chefs.find(),course=None,chef=None,is_vegetarian=None)
    return render_template("index.html", username='',
                           recipes=db_recipes.find(),courses=db_courses.find(),chefs=db_chefs.find(),course=None,chef=None)
 

@app.route('/logout')
def logout():
    """ Log out button pressed """
    session['username'] = ''
    return redirect(url_for('index'))


@app.route('/courses')
def courses():
    """ Manage the Courses page """
    if 'username' in session:
        return render_template("courses.html",
                        courses=db_courses.find(), username=session['username'])
    else:
       return render_template("courses.html",
                            courses=db_courses.find(), username='')


@app.route('/chefs')
def chefs():
    """ Manage the chefs page """
    if 'username' in session:
        return render_template("chefs.html", chefs=db_chefs.find(), username=session['username'])
    else:
        return render_template("chefs.html", chefs=db_chefs.find(), username='')
        

@app.route('/add_recipe')
def add_recipe():
    """ Add a recipe page """
    if 'username' in session:
        return render_template('add_recipe.html',
                           courses=db_courses.find(),
                           chefs=db_chefs.find(), username=session['username'])
    else:
       return render_template('add_recipe.html',
                           courses=db_courses.find(),
                           chefs=db_chefs.find(), username='')
                               

@app.route('/add_recipe', methods = ['GET','POST'])
def insert_recipe():
        if request.method == 'POST':
            recipe ={'recipe_name': request.form.get('recipe_name'),
                'recipe_description': request.form.get('recipe_description'),
                'recipe_ingredients': request.form.get('recipe_ingredients'),
                'recipe_method': request.form.get('recipe_method'),
                'recipe_course': request.form.get('recipe_course'),
                'recipe_chef': request.form.get('recipe_chef'),
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
    chefs=db_chefs.find())
    
@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    if 'username' in session:
        return render_template('display_recipe.html', username=session['username'],
        recipe=db_recipes.find_one({'_id': ObjectId(recipe_id)}))
    else:
        return render_template('display_recipe.html', username='',
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
        'recipe_chef': request.form.get('recipe_chef'),
        'recipe_image_url': request.form.get('recipe_image_url'),
        'recipe_is_vegetarian':request.form.get('is_vegetarian'),
        'recipe_is_vegan':request.form.get('is_vegan'),
        'recipe_is_glutenfree':request.form.get('is_glutenfree'),
        'recipe_entered_by' :session['username']
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
                           recipes=db_recipes.find(),courses=db_courses.find(),chefs=db_chefs.find(),course=None,chef=None)

            flash('Incorrect password')  
    if 'username' in session:
        return render_template('login.html', username=session['username'])
    else:
        return render_template('login.html', username='')

                       
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = db_users
        existing_user = users.find_one({'name' : request.form['username']})
        password1 = request.form.get('pass')
        password2 = request.form.get('pass2')
       
        if password1 != password2:
            flash('The passwords do not match')  
        elif existing_user is not None:
            flash('That username already exists!')  
        elif existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
    return render_template('register.html', username='')
    
@app.route('/search')
def search():
    """ Route for the search"""
    query = request.args['query']
    recipes = db_recipes.find({'$text': {'$search': query }})
    if 'username' in session:
        return render_template("index.html", username=session['username'],
                               recipes=recipes,courses=db_courses.find(),chefs=db_chefs.find(),course=None,chef=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)
    return render_template("index.html", username='',
                            recipes=recipes,courses=db_courses.find(),chefs=db_chefs.find(),course=None,chef=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)

    
@app.route('/recipe_filtered', methods = ['POST'])
def recipe_filtered():
    if request.form.get('reset_button') == 'reset':
        print("Reset button pressed...")
        recipes=db_recipes.find()
        if 'username' in session:
            return render_template("index.html", username=session['username'],
                               recipes=recipes,courses=db_courses.find(),chefs=db_chefs.find(),course=None,chef=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)
        return render_template("index.html", username='',
                               recipes=recipes,courses=db_courses.find(),chefs=db_chefs.find(),course=None,chef=None,is_vegetarian=None,is_vegan=None,is_glutenfree=None)
                         
    else:
        print("recipe_filtered...")
        recipes=db_recipes
        course = request.form.get('course_name')
        chef = request.form.get('chef_name')
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
        if chef is not None:
            filter_by['recipe_chef'] = chef
            print("filter_by: ",filter_by)
        print("filter_by type",type(filter_by))
        recipes=db_recipes.find({"$and":[ filter_by ]})
    
    
        if 'username' in session:
            return render_template("index.html", username=session['username'],
                               recipes=recipes,courses=db_courses.find(),chefs=db_chefs.find(),course=course,chef=chef,is_vegetarian=vegetarian,is_vegan=vegan,is_glutenfree=glutenfree)
        return render_template("index.html", username='',
                               recipes=recipes,courses=db_courses.find(),chefs=db_chefs.find(),course=course,chef=chef,is_vegetarian=vegetarian,is_vegan=vegan,is_glutenfree=glutenfree)
                         
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
    
@app.route('/get_chefs')
def get_chefs():
    if 'username' in session:
        return render_template("chefs.html", chefs=db_chefs.find(), username=session['username'])
    else:
        return render_template("chefs.html", chefs=db_chefs.find(), username='')


@app.route('/delete_chefs/<chef_id>', methods=["POST"])
def delete_chef(chef_id):
    db_chefs.remove({'_id': ObjectId(chef_id)})
    return redirect(url_for('get_chefs'))

@app.route('/edit_chef/<chef_id>')
def edit_chef(chef_id):
    return render_template('edit_chef.html',
    chef=db_chefs.find_one({'_id': ObjectId(chef_id)}))


@app.route('/update_chef/<chef_id>', methods=['POST'])
def update_chef(chef_id):
    chef = db_chefs
    chef.update( {'_id': ObjectId(chef_id)},
    {
        'chef_name': request.form.get('chef_name'),
        'chef_entered_by': session['username']
    })
    return redirect(url_for('get_chefs'))

@app.route('/insert_chef', methods=['POST'])
def insert_chef():
    chef_doc = {
        'chef_name': request.form.get('chef_name'),
        'chef_entered_by': session['username']
    }
    db_chefs.insert_one(chef_doc)
    return redirect(url_for('get_chefs'))

@app.route('/add_chef')
def add_chef():
    if 'username' in session:
        return render_template('add_chef.html', username=session['username'])
    else:
        return render_template('add_chef.html', username='')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)