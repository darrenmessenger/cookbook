# Cookbook

<img src="static/images/cookbook home page.png">

## Reason For Project

This project has been built for the Practical Python and Data-Centric Development Milestone Project.
The brief was to build a full-stack site that allows users to manage a common dataset about a particular domain.

Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.
The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit from the collection of the dataset as a whole.

The main technologies that are to be used for this project are HTML, CSS, JavaScript, Python+Flask, MongoDB.

I have decided to create a cookbook web application that allows users to store and easily access cooking recipes. Recipes would include fields such as ingredients, preparation steps, required tools, cuisine, etc.

There was a number of suggested features including:

Create the backend code and frontend form(s) to allow users to add new recipes to the site, edit them and delete them.

Create the backend and frontend functionality for users to locate recipes based on the recipe's fields. You may choose to create a full search functionality, or just a directory of recipes.

Provide results in a manner that is visually appealing and user friendly.


The wireframes for this website can be found in the repository within Github in the directory "assets/images/Wireframes", 
or you can click [here](https://github.com/darrenmessenger/simon-game/tree/master/assets/images/Wireframes).

The live website can be found [here](https://darrenmessenger.github.io/simon-game/).

### User Stories

- If I look at the game when the page loads I will see an information 'banner' telling me to press the 'Start/Reset' button to begin.  
- I press a coloured panel and I hear a sound that represents the panel and the panel that I pressed vibrates.
- I press the 'Start/Reset' button and I can hear and see a start up sequence. 
- After the start up sequence has finished a random panel makes a sound and vibrates. 
- If I correctly copy the random panel sequence that the game displayed then I will see an information message with a random statement and another random panel will be added to the sequence. 
- I can see a countdown timer that starts as soon as the random panel or panels are displayed. 
- If I do not press a panel before the countdown gets to zero then the game is finished and I will hear a buzzer and an information message stating which round I achieved. 
- If I copy the random sequence correcly each time the counter will increase showing me which round I am on. 
- I can see at any time which round I am on by looking at the counter. 
- If I copy the random sequence incorrectly then I will hear a buzzer and an information message stating which round I achieved. 
- If I hear the buzzer that means the game has ended and I will see a flashing information message telling me to press the 'Start/Reset' button.
- If I want to restart the game at any time then I can press the 'Start/Reset' button. 
- If I keep copying the sequence of random panels correctly the sequence will increase by one each round.
- If I keep copying the sequence of random panels correctly the sequence could get quite long as there isn't an end to the game unless a mistake is made or the game times out.
- If I beat the highest score then I want the display of the 'Highest Score' to be updated with my current score. 
- If the Game is showing the next sequence of colours do not let the user press any panel until the sequence has finished. 
 
### Process

I went through the user stories and wireframes before embarking on the actual coding of the project to ensure I had a good idea of how to approach things. 

## Features

#### Main Page
On the main page there is a background image of some random numbers. The background image seemed to suit the Simon game. 
The two main sections have this background but I have put an opaque overlay over the background image, one in blue and the other in yellow. 
I chose these colours as they suited the colours of the actual Simon game (red, blue, green, yellow).

#### Navigation:
There is a static header at the top of the page which includes some menu items to take you to different parts of the page. 
I have incorporated some jquery code that I found on stackoverflow that allows the page to scroll smoothly when a navigation link is clicked. 
On small screens the navigation menu disappears and a bootstrap burger button appears so that the menu can be toggled on or off. 

#### About:
There is an about section that utilises the bootstrap grid layout. The description of the Simon game is a summary taken from Wikipedia. 
There is also a 'Read more...' with a link to Wikipedia if the user wants to read more about the game. 

#### Simon Game:
This section utilises the bootstrap grid layout. 

The game itself uses has different colour panels withing a large circle to imitate the game. There is a counter and a 'Start/Reset' button within the circle as well. 

When a user clicks on a button or a panel the relevant function is called from the script.js file. There are a number of functions that deal with every aspect of the game. 

The game utilises Animate.css which creates CSS animations. I used it to create a 'vibrating' effect when each button is clicked. 

Each of the User Stories were looked at to make sure that the game functioned correctly. The design and functionality of the game was based on the User Stories. 

#### Contact Me:
This section utilises the bootstrap grid layout. There is a form to allow the user to enter details so that they may contact me if they like the game and want to give me a project or want to discuss something.
All the details are very clear using descriptive placeholders. 
I have used [EmailJS](http://www.emailjs.com/) so that when the user presses 'submit' I will receive an email and see the details of what the user has typed in. 
Once the email has been sent successfully the user will see a message box and the input fields will be blanked out. 

I have also used [Google Maps API](https://developers.google.com/maps/documentation/javascript/tutorial) to show a map of my location. If the user clicks on the Marker then the map will zoom in. 

#### Footer:
At the bottom of the page there are links to various social media including Twitter, LinkedIN, GitHub, YouTube and Instagram. 
When the links are clicked then a new page is opened up showing the social media page. 

## Technologies Used

The following technologies have all been used during the coding of this project:

- [Bootstrap](https://getbootstrap.com/) I used bootstrap 3.3.7 to organise the grid layout of the site. 
- [JQuery](https://jquery.com/). This was used for the gaming functionality. 
- [SASS](https://sass-lang.com/guide) I have used SCSS files with Preprocessing, Partials, Variables, Imports, Mixins, Extend, and Operators. 
- [EmailJS](http://www.emailjs.com/) When the contact form is submitted I utilised emailJS to send me an actual email to my email address. 
- [Google Fonts](https://fonts.google.com/) I chose the 'Nunito' font as it suited my project. 
- [FontAwesome](https://fontawesome.com/) I used FontAwesome for the icons shown in the footer for the social links. 
- [Animate.css](https://daneden.github.io/animate.css/) This was useful to imitate a 'vibrating' panel on the game. 
- [Google Maps API](https://developers.google.com/maps/documentation/javascript/tutorial) This showed where I am based. 
- [GitHub](https://github.com/darrenmessenger/simon-game) I used GitHub for version control and to publish the site using GitHub Pages. 

## Testing

The HTML and CSS code used on this project has been tested using The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) 
and The [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input).

The project has been tested on Google Chrome (desktop and mobile versions), Mozilla Firefox and Microsoft Edge. 

Every other aspect of the site has been tested as described below.

### Responsive Testing
I utilised Bootstrap so that the whole site would be responsive on different platforms. 

On a large screen the full navigation menu is displayed and the game appears next to the about section. The map of my location appears next to the contact form. 

On a medium screen the full navigation menu is displayed but the game appears underneath the about section. The map also appears underneath the contact form. 

On a small screen the menu items disappear and a bootstrap burger button appears which, when clicked, displays the menu items on their own row. If clicked again the menu will disappear again.  
The game is displayed beneath the about section and the map appears beneath the contact form as it did on a medium screen. 

### Header and Navigation

On the top of the page there is a navigation bar with 4 menu items. Each menu item has been tested on each page to ensure it takes the user to the correct area of the page. 
The page scrolled smoothly when a navigation link is clicked as it should. 
When each menu item is hovered over there is a transition to a different colour so that the user can see which menu item is being hovered over. 

### About

The 'Read more...' link was checked to make sure a new page was opened with the Wikipedia page. The about section appeared in the correct place on the page when tested responsively. 

### Simon Game

The game appeared in the correct place on the page when tested responsively. 

The game has been tested extensively by both me and my family!.

I went through each of the User Stories to make sure that they worked as expected. 

| User Story | Result |
| ---------- | ------ |
| If I look at the game when the page loads I will see an information 'banner' telling me to press the 'Start/Reset' button to begin. | **PASSED** |
| I press a coloured panel and I hear a sound that represents the panel and the panel that I pressed vibrates. | **PASSED** |
| I press the 'Start/Reset' button and I can hear and see a start up sequence. | **PASSED** |
| After the start up sequence has finished a random panel makes a sound and vibrates. | **PASSED** |
| If I correctly copy the random panel sequence that the game displayed then I will see an information message with a random statement and another random panel will be added to the sequence. | **PASSED** |
| I can see a countdown timer that starts as soon as the random panel or panels are displayed. | **PASSED** |
| If I do not press a panel before the countdown gets to zero then the game is finished and I will hear a buzzer and an information message stating which round I achieved. | **PASSED** |
| If I copy the random sequence correcly each time the counter will increase showing me which round I am on. | **PASSED** |
| I can see at any time which round I am on by looking at the counter. | **PASSED** |
| If I copy the random sequence incorrectly then I will hear a buzzer and an information message stating which round I achieved. | **PASSED** |
| If I hear the buzzer that means the game has ended and I will see a flashing information message telling me to press the 'Start/Reset' button. | **PASSED** |
| If I want to restart the game at any time then I can press the 'Start/Reset' button. | **PASSED** |
| If I keep copying the sequence of random panels correctly the sequence will increase by one each round. | **PASSED** |
| If I keep copying the sequence of random panels correctly the sequence could get quite long as there isn't an end to the game unless a mistake is made or the game times out. | **PASSED** |
| If I beat the highest score then I want the display of the 'Highest Score' to be updated with my current score. | **PASSED**|
| If the Game is showing the next sequence of colours do not let the user press any panel until the sequence has finished. | **PASSED** |

### Contact Me

The contact section and the map appeared in the correct place on the page when tested responsively. 

There are 3 fields that need to be entered by the user. Each field was tested to make sure the user entered data in that field. 
If the user didn't enter data in each field then the submit button won't submit the data because an error message appears. 
When all the fields have been entered and the Send Request button is pressed I made sure an email is received in my inbox. 
There was also a message box that appeared when emailJS sent the email successfully. If it wasn't sent successfully then an error message would be displayed. 

The map appeared as it should and the marker pinpointed my location. When the marker was clicked it zoomed into my location so that it showed a little more detail. 

### Footer

There are links to social pages within the footer. Each link was clicked to make sure it loads up a new page with the correct social page. 

### Jasmine Testing 

I did look into Jasmine testing but realised it is mainly useful when a function or the DOM returns a value. 

This project did not give me the opportunity to use Jasmine testing as the functions simply ran without returning a value or called another function. 

## Deployment 

This project was deployed through GitHub Pages. The process was simple and involved going to my repository for this project and clicking on the settings icon. 

I scrolled down to the GitHub Pages section and picked 'Master Branch' as the source, and saved it. The URL of the published site was then displayed in that same section. 

Anyone can download the project or clone it from GitHub [here](https://github.com/darrenmessenger/simon-game) 

The live website can be found [here](https://darrenmessenger.github.io/simon-game/).

### Cloning

If you wish to clone this project then you can click on the green 'Clone or download' button on [this](https://github.com/darrenmessenger/simon-game) page, and then download the .zip file. 

Unzip the file into the directory you prefer on your computer or cloud drive and then import it into your favourite IDE. 

You will need to install Bcrypt:
sudo pip3 install bcrypt


## Credits

I would like to thank all of the Code Institute students that helped throughout this project on Slack. 

### Content

- The text from the about section was received from [Wikipedia](https://en.wikipedia.org/wiki/Simon_(game)).

## Media

- The background image was downloaded from [ShutterStock](https://www.shutterstock.com/).
- The audio sounds (beeps and failure sounds) were found on [Sound Jay](https://www.soundjay.com/).
