# Cookbook

<img src="static/images/cookbook home page.png">

## Reason For Project

This project has been built for the Practical Python and Data-Centric Development Milestone Project.
The brief was to build a full-stack site that allows users to manage a common dataset about a particular domain.

Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.
The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit 
from the collection of the dataset as a whole.

The main technologies that are to be used for this project are HTML, CSS, JavaScript, Python+Flask, MongoDB.

I have decided to create a cookbook web application that allows users to store and easily access cooking recipes. Recipes would include fields such as 
ingredients, preparation steps, required tools, cuisine, etc.

There was a number of suggested features including:

- Create the backend code and frontend form(s) to allow users to add new recipes to the site, edit them and delete them.

- Create the backend and frontend functionality for users to locate recipes based on the recipe's fields. You may choose to create a full search functionality, or just a directory of recipes.

- Provide results in a manner that is visually appealing and user friendly.


The wireframes for this website can be found in the repository within Github in the directory "static/images/Wireframes", 
or you can click [here](https://github.com/darrenmessenger/cookbook/tree/master/static/images/Wireframes).

The live website can be found [here](https://python-cookbook-project-dm.herokuapp.com/).

### Database Schema
[Mongodb](https://cloud.mongodb.com/v2/5c64623aa6f239113e199d4c#metrics/replicaSet/5c6484dfa6f239229159aacd/explorer/cookbook) was used to create the database for the project.
The final database ERD can be found in the folder [here](https://github.com/darrenmessenger/cookbook/tree/master/static/images/ERD).
The final database consists of 5 collections, categories, chefs, courses, recipes and users. Details are shown below: 

#### categories
- _id (ID of the category)
- category_name (Name of the category)

#### chefs
- _id (ID of chefs)
- chef_entered_by (The user that originally entered the chef)
- chef_name (Name of the chef)

#### courses
- _id (ID of courses)
- course_name (The name of the starter)

#### recipes
- _id (ID of the recipe)
- recipe_name (The name of the recipe)
- recipe_description (The description of the recipe)
- recipe_ingredients (The recipe ingredients)
- recipe_method (The steps involved with how the recipe is made)
- recipe_course (Which course this recipe belongs to)
- recipe_chef (Which chef originally made up this recipe)
- recipe_image_url (The URL of the image so that an image can be seen)
- recipe_is_vegetarian (Is the recipe vegetarian)
- recipe_is_vegan (Is the recipe vegan )
- recipe_is_glutenfree (Is the recipe gluten free)
- recipe_entered_by (Which user entered the recipe)

#### users
- _id (ID of courses)
- name (The name of the registered user)
- password (The password that the user entered when they registered)

 
### User Stories

- Home Page:
- I should see a banner with some famous quotes on top of some changing food images.
- There should be a Navbar with a Login and Register link.
- I should see a welcome message and a link to login or register to the the site. 
- I should see a selection of recipes that myself or other users have uploaded. 
- I should be able to filter the recipes by Course, Chef, Vegan, Vegetarian or wether the recipe is Gluten Free.
- I should be able to either enter one filter or any combination of filters. 
- I should be able to press a button to filter the recipes based on my filters. 
- I should be able to press a button to reset the filters. 
- I should be able to enter a keyword to search the recipe.
- If I press enter after entering a keyword in the search box the recipe should be displayed.
- If I hover over a recipe it should be highlighted. 
- If I press the red arrow on the recipe it should open a new page with all the details of the recipe.
- Recipe Display Page:
- The selected recipe details should be displayed when this page is loaded.
- If the recipe was entered by me then I should be able to edit or delete the recipe via buttons at the bottom of the recipe. 
- If the recipe was not entered by me then I should only be able to view the recipe. 
- If I click on the 'Edit' button then the 'Edit Recipe' page should load so that the recipe can be edited. 
- If I click on the 'Delete' button then the recipe should be deleted and the home page should be loaded. 
- Add Recipe Page:
- When the page is loaded I should see the descriptions of each section that can be entered. 
- I should be able to enter the details of the recipe.
- If there is a drop down box I should be able to select the correct item.
- I should be able to enter the URL of the image of the recipe.
- If I enter the wrong image URL or leave it blank a default image should be displayed on the main page.
- After I have entered the details of the recipe I should be able to press a button to add the recipe and be returned to the main page. 
- Edit Recipe Page:
- The selected recipe details should be displayed when this page is loaded with editable fields.
- I should be able to edit any part of the recipe.
- If I press the 'Update Recipe' button my changes should be saved to the database.
- If I make changes and I press the 'Reset' button my changes should roll back to what they were before.
- If I click on the 'Delete' button the recipe should be deleted and the home page should be loaded. 
- Manage Courses Page:
- If the 'Manage Courses' menu item is seleted from the navigation bar then then a page should be displayed that allows me to edit, add or delete courses.
- When the page loads all of the courses should be listed.
- I should be able to delete a course.
- I should be able to edit a course. 
- If I click on 'Edit' then a new page should be loaded with details of the course so that it can be edited.
- If I click on 'Del' then the course should be deleted and the page refreshed.
- If I click on 'Add Course' then a new page should be loaded so that I can enter a new course.
- Add Course Page:
- When the page is loaded the Course Name should be blank so I can enter a new Course Name.
- I should be able to enter a new Course Name and press a button so that the course is added to the database.
- If I add a new course then I should be returned to the list of courses available.
- Edit Course Page:
- When the page is loaded the Course Name should be displayed and it should be editable.
- If I edit a course then I should be able to press a button to save my changes and be returned to the list of courses available.
- I should be able to cancel my changes and be returned to the list of courses available.
- Manage Chefs Page:
- If the 'Manage Chefs' menu item is seleted from the navigation bar then then a page should be displayed that allows me to edit, add or delete chefs.
- When the page loads all of the Chefs should be listed.
- I should be able to delete a chef.
- I should be able to edit a chef. 
- If I click on 'Edit' then a new page should be loaded with details of the chef so that it can be edited.
- If I click on 'Del' then the chef should be deleted and the page refreshed.
- If I click on 'Add Chef' then a new page should be loaded so that I can enter a new chef.
- Add Chef Page:
- When the page is loaded the Chef Name should be blank so I can enter a new Chef Name.
- I should be able to enter a new Chef Name and press a button so that the chef is added to the database.
- If I add a new chef then I should be returned to the list of chefs available.
- Edit Chefs Page:
- When the page is loaded the Chefs Name should be displayed and it should be editable.
- If I edit a chef then I should be able to press a button to save my changes and be returned to the list of chefs available.
- I should be able to cancel my changes and be returned to the list of chefs available.
- Footer:
- There should be a footer at the bottom of the page.
- When the social links in the footer are hovered over they should change colour to red. 
- When the social links are clicked a new tab should open showing the relevant website. 
- Navbar:
- If I am not logged in I should see a 'Log In' and a 'Register' menu option.
- If I click the Login link it should open the Login page. 
- If I click the Register link it should open the Register page. 
- If I click on the Cookbook title in the navbar it should always take me back to the home page.
- If I am logged in I should see a 'Add Recipe', 'Manage Courses', 'Manage Chefs' and 'LogOut' menu options. 
- If I click on the 'Add Recipe' menu option it should open the 'Add Recipe' page.
- If I click on the 'Manage Courses' menu option it should open the 'Manage Courses' page.
- If I click on the 'Manage Chefs' menu option it should open the 'Manage Chefs' page.
- If I click on the 'LogOut' menu option it should log me out and take me to the home page.
- Login Page:
- If I do not log in then I should be able to browse recipes as a guest. 
- If I do not log in then I should not be able to delete or edit any recipes. 
- If I do not log in then I shouldn't be able to add any recipes, chefs or courses. 
- If I do log in then I should be able to edit or delete any courses, chefs or recipes that I have entered. 
- If I  log in then I shouldn't be able to edit or delete any recipes that someone else has entered. 
- When the Login page is loaded it should show a blank Username and Password.
- I should be able to see a link to 'Sign Up' if I haven't done so already.
- If I click on the 'Sign Up' link it should open the 'Register' page. 
- If I enter my Username and Password correctly it should navigate to the home page with a new welcome message that includes my username.
- If I enter an incorrect username I should see an error message stating that the username is incorrect.
- If I enter the correct username but incorrect password I should see an error message stating that the password is incorrect.


### Process

I went through the user stories and wireframes before embarking on the actual coding of the project to ensure I had a good idea of how to approach things. 

## Features
Throughout the project I have use MaterializeCSS as it is a modern, responsive front-end framework. It has ensured that every page of the project is 
consistent in its design and layout. Next to the title on the browser tab I have added a favicon of a knife and fork. 

#### Main Page
On the main page there is a slide showing different images with some 'foody' quotes that rotate. Once the user has logged in then there will be a welcome 
message showing their username. If the user scrolls down they will see all of the recipes displayed with a brief description. If they want to see
more details then they can press the button on the card and a new page will be displayed showing all of the details of the recipe. They can also
filter the recipes using either the course, chef, vegetarian, vegan or gluten free.

#### Display Recipe:
This page shows the details and the image of the recipe. The user will only see the Edit or Delete button if it was their username 
that entered the recipe in the first place.

#### Add Recipe:
This page is used to add a recipe. Details can be entered along with a URL image of the recipe. There is a button at the botton so that the recipe
can be added. 

#### Edit Recipe:
This page is used to edit a recipe. When the page is loaded the current details are loaded and any of these can be edited. There is a button at the botton so that the recipe
can be updated. There is also a reset button that can be pressed so that any changes that the user has entered are reversed.

#### Manage Courses:
This page is used to edit or delete the courses that are stored on the database. Any user can update or delete an existing course.

#### Manage Chefs:
This page is used to edit or delete the chefs that are stored on the database. The user will only see the Edit or Delete button if it was their username 
that entered the chef in the first place. You can also press a button to add a new chef.

#### Navigation:
There is a  header at the top of the page which includes some menu items to take you to different parts of the website. 
On small screens the navigation menu disappears and a burger icon button appears so that the menu can be toggled on or off. 
When each menu item is hovered over there is a transition to a different colour so that the user can see which menu item is being hovered over. 

#### Footer:
At the bottom of the page there are links to various social media including Twitter, LinkedIN, GitHub and Instagram. 
When the links are clicked then a new page is opened up showing the social media page. 

## Technologies Used

The following technologies have all been used during the coding of this project:

- [Materializecss](https://materializecss.com/) The whole project is built using materializecss as it is responsive and enables fast development. 
- [JQuery](https://jquery.com/). This was used for the gaming functionality. 
- [SASS](https://sass-lang.com/guide) I have used SCSS files. 
- [Google Fonts](https://fonts.google.com/) Google fonts are used in the project. 
- [FontAwesome](https://fontawesome.com/) I used FontAwesome for the icons shown in the footer for the social links. 
- [GitHub](https://github.com/darrenmessenger/cookbook) I used GitHub for version control. 
- [Heroku](https://python-cookbook-project-dm.herokuapp.com) I used Heroku to publish the site. 
- [Mongodb](https://cloud.mongodb.com/v2/5c64623aa6f239113e199d4c#metrics/replicaSet/5c6484dfa6f239229159aacd/explorer/cookbook) Mongodb was used to create the database for the project.

 
## Testing

The HTML and CSS code used on this project has been tested using The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) 
and The [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input).

The project has been tested on Google Chrome (desktop and mobile versions), Mozilla Firefox and Microsoft Edge. 

Every other aspect of the site has been tested as described below.

### Responsive Testing
I utilised MaterializeCSS so that the whole site would be responsive on different platforms. 

On a large and medium screen the full navigation menu is displayed. The recipes will appear as two per row.

On a small screen the menu items disappear and a burger button appears which, when clicked, displays the menu items.
The recipes will appear as one per row.

### General Testing

I went through each of the User Stories to make sure that they worked as expected. 

| User Story | Result |
| ---------- | ------ |
| Home Page: |  |
| There should be a Navbar with a Login and Register link.| **PASSED** |
| I should see a welcome message and a link to login or register to the the site. | **PASSED** |
| I should see a selection of recipes that myself or other users have uploaded. | **PASSED** |
| I should be able to filter the recipes by Course, Chef, Vegan, Vegetarian or wether the recipe is Gluten Free.| **PASSED** |
| I should be able to either enter one filter or any combination of filters. | **PASSED** |
| I should be able to press a button to filter the recipes based on my filters. | **PASSED** |
| I should be able to press a button to reset the filters. | **PASSED** |
| I should be able to enter a keyword to search the recipe.| **PASSED** |
| If I press enter after entering a keyword in the search box the recipe should be displayed.| **PASSED** |
| If I hover over a recipe it should be highlighted. | **PASSED** |
| If I press the red arrow on the recipe it should open a new page with all the details of the recipe.| **PASSED** |
| Recipe Display Page:|  |
| The selected recipe details should be displayed when this page is loaded.| **PASSED** |
| If the recipe was entered by me then I should be able to edit or delete the recipe via buttons at the bottom of the recipe. | **PASSED** |
| If the recipe was not entered by me then I should only be able to view the recipe. | **PASSED** |
| If I click on the 'Edit' button then the 'Edit Recipe' page should load so that the recipe can be edited. | **PASSED** |
| If I click on the 'Delete' button then the recipe should be deleted and the home page should be loaded. | **PASSED** |
| Add Recipe Page:|  |
| When the page is loaded I should see the descriptions of each section that can be entered. | **PASSED** |
| I should be able to enter the details of the recipe.| **PASSED** |
| If there is a drop down box I should be able to select the correct item.| **PASSED** |
| I should be able to enter the URL of the image of the recipe.| **PASSED** |
| If I enter the wrong image URL or leave it blank a default image should be displayed on the main page.| **PASSED** |
| After I have entered the details of the recipe I should be able to press a button to add the recipe and be returned to the main page. | **PASSED** |
| Edit Recipe Page:|  |
| The selected recipe details should be displayed when this page is loaded with editable fields.| **PASSED** |
| I should be able to edit any part of the recipe.| **PASSED** |
| If I press the 'Update Recipe' button my changes should be saved to the database.| **PASSED** |
| If I make changes and I press the 'Reset' button my changes should roll back to what they were before.| **PASSED** |
| If I click on the 'Delete' button the recipe should be deleted and the home page should be loaded.| **PASSED** | 
| Manage Courses Page:|  |
| If the 'Manage Courses' menu item is seleted from the navigation bar then then a page should be displayed that allows me to edit, add or delete courses.| **PASSED** |
| When the page loads all of the courses should be listed.| **PASSED** |
| I should be able to delete a course.| **PASSED** |
| I should be able to edit a course.| **PASSED** | 
| If I click on 'Edit' then a new page should be loaded with details of the course so that it can be edited.| **PASSED** |
| If I click on 'Del' then the course should be deleted and the page refreshed.| **PASSED** |
| If I click on 'Add Course' then a new page should be loaded so that I can enter a new course.| **PASSED** |
| Add Course Page:|  |
| When the page is loaded the Course Name should be blank so I can enter a new Course Name.| **PASSED** |
| I should be able to enter a new Course Name and press a button so that the course is added to the database.| **PASSED** |
| If I add a new course then I should be returned to the list of courses available.| **PASSED** |
| Edit Course Page:|  |
| When the page is loaded the Course Name should be displayed and it should be editable.| **PASSED** |
| If I edit a course then I should be able to press a button to save my changes and be returned to the list of courses available.| **PASSED** |
| I should be able to cancel my changes and be returned to the list of courses available.| **PASSED** |
| Manage Chefs Page:|  |
| If the 'Manage Chefs' menu item is seleted from the navigation bar then then a page should be displayed that allows me to edit, add or delete chefs.| **PASSED** |
| When the page loads all of the Chefs should be listed.| **PASSED** |
| I should be able to delete a chef.| **PASSED** |
| I should be able to edit a chef. | **PASSED** |
| If I click on 'Edit' then a new page should be loaded with details of the chef so that it can be edited.| **PASSED** |
| If I click on 'Del' then the chef should be deleted and the page refreshed.| **PASSED** |
| If I click on 'Add Chef' then a new page should be loaded so that I can enter a new chef.| **PASSED** |
| Add Chef Page:|  |
| When the page is loaded the Chef Name should be blank so I can enter a new Chef Name.| **PASSED** |
| I should be able to enter a new Chef Name and press a button so that the chef is added to the database.| **PASSED** |
| If I add a new chef then I should be returned to the list of chefs available.| **PASSED** |
| Edit Chefs Page:|  |
| When the page is loaded the Chefs Name should be displayed and it should be editable.| **PASSED** |
| If I edit a chef then I should be able to press a button to save my changes and be returned to the list of chefs available.| **PASSED** |
| I should be able to cancel my changes and be returned to the list of chefs available.| **PASSED** |
| Footer:|  |
| There should be a footer at the bottom of the page.| **PASSED** |
| When the social links in the footer are hovered over they should change colour to red. | **PASSED** |
| When the social links are clicked a new tab should open showing the relevant website.| **PASSED** | 
| Navbar:|  |
| If I am not logged in I should see a 'Log In' and a 'Register' menu option.| **PASSED** |
| If I click the Login link it should open the Login page.| **PASSED** | 
| If I click the Register link it should open the Register page.| **PASSED** | 
| If I click on the Cookbook title in the navbar it should always take me back to the home page.| **PASSED** |
| If I am logged in I should see a 'Add Recipe', 'Manage Courses', 'Manage Chefs' and 'LogOut' menu options.| **PASSED** | 
| If I click on the 'Add Recipe' menu option it should open the 'Add Recipe' page.| **PASSED** |
| If I click on the 'Manage Courses' menu option it should open the 'Manage Courses' page.| **PASSED** |
| If I click on the 'Manage Chefs' menu option it should open the 'Manage Chefs' page.| **PASSED** |
| If I click on the 'LogOut' menu option it should log me out and take me to the home page.| **PASSED** |
| Login Page:|  |
| If I do not log in then I should be able to browse recipes as a guest. | **PASSED** |
| If I do not log in then I should not be able to delete or edit any recipes. | **PASSED** |
| If I do not log in then I shouldn't be able to add any recipes, chefs or courses. | **PASSED** |
| If I do log in then I should be able to edit or delete any courses, chefs or recipes that I have entered. | **PASSED** |
| If I  log in then I shouldn't be able to edit or delete any recipes that someone else has entered. | **PASSED** |
| When the Login page is loaded it should show a blank Username and Password.| **PASSED** |
| I should be able to see a link to 'Sign Up' if I haven't done so already.| **PASSED** |
| If I click on the 'Sign Up' link it should open the 'Register' page.| **PASSED** | 
| If I enter my Username and Password correctly it should navigate to the home page with a new welcome message that includes my username.| **PASSED** |
| If I enter an incorrect username I should see an error message stating that the username is incorrect.| **PASSED** |
| If I enter the correct username but incorrect password I should see an error message stating that the password is incorrect.| **PASSED** |


### Jasmine Testing 

This project did not give me the opportunity to use Jasmine testing as the functions simply ran without returning a value or called another function. 

## Deployment 

This project was deployed through Heroku. 

Following steps were taken to deploy the website:

In app.py I changed debug=True to debug=False as debug=True is used for debugging during development. 
debug=False is is for deployment to a production server.

In Cloud9 open up a command line and type ‘heroku’. That will show that heroku is already installed. 

Type ‘heroku login -i’ to login to your heroku account. Type ‘heroku apps’ to show the apps in your account. 

To create an app on Heroku you can either do it directly on Heroku or run the following command:
```
heroku apps:create python-cookbook-project-dm
```

Copy the heroku git URL from the setting page of heroku and enter the following command on Cloud9:
```
git remote add heroku https://git.heroku.com/thorin-and-company-dm.git
```

Then run the following command to see the remote git attached to your project:
```
git remote -v
```

If you haven’t added the files to Heroku yet then you will have to run the following command:
```
git add .
```
And then commit the changes:
```
git commit -m “Deployment to Heroku”
```
Type the following command to push the project to heroku:
```
git push -u heroku master
```

To create a requirements.txt file run the following command:
```
sudo pip3 freeze --local > requirements.txt
```
Then:
```
git add requirements.txt
```
```
git commit -m "Add requirements file"
```
```
git push -u heroku master
```
We then need to create a Procfile with the following commands:
```
echo web: python run.py > Procfile
```
```
git add Procfile
```
```
git commit -m "Add Procfile"
```
```
git push -u heroku master
```
In heroku app, inside the settings, clicked Config Vars, and set IP, PORT and environment variable MONGO_URI.
Clicked 'Open app' and the website was up and running.



Anyone can download the project or clone it from GitHub [here](https://github.com/darrenmessenger/cookbook) 

The live website can be found [here](http://python-cookbook-project-dm.herokuapp.com/).

### Cloning

If you wish to clone this project then you can click on the green 'Clone or download' button on [this](https://github.com/darrenmessenger/cookbook) page, and then download the .zip file. 

Unzip the file into the directory you prefer on your computer or cloud drive and then import it into your favourite IDE. 

Clone the repository
```
git clone https://github.com/darrenmessenger/cookbook.git
```

Move into the folder
```
cd directoty-name
```

You will need to install the dependencies found in the requirements.txt file:
```
pip3 freeze --local > requirements.txt
```
 
Then run:
```
sudo pip3 install flask-pymongo 
```
```
sudo pip3 install dnspython
```

To run the project locally use:
```
python3 app.py runserver
```

### Keeping MongoDB Password Private

Go to the MongoDB Atlas DB and click on ‘Connect’. Select ‘Connect Your Application’ and then click on the ‘Short SRV Connection String’ and copy the text. 

Go to cloud9 and enter in a command terminal:
```
Cd ..
nano .bashrc
```

Near the top of the opened file enter:
```
export MONGO_URI="mongodb+srv://root:r00tUser@cluster0-nogor.mongodb.net/cookbook?retryWrites=true&w=majority"
```    
Where the address in quotes is what you have just copied. Remember to change the database name and the password. Press CTRL X to exit, Y to save then Enter for the filename.

Close the Terminal and reopen it so that the changes take effect.

Type the following in a terminal to show the connection string:
```
echo $MONGO_URI
```
Edit app.py with the following so that you can connect to MongoDB:
```
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)
```

## Credits

I would like to thank all of the Code Institute students that helped throughout this project on Slack. 

### Content

- The recipes were found from the BBC food website and Jamie Olivers.

## Media

- The background images was downloaded from [ShutterStock](https://www.shutterstock.com/).

