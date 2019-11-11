Introduction?

## Table of Contents
1. UX
    #### User Stories
    #### Wireframes
2. Features
    #### Existing Features
    #### Future Features
3. List of Technologies
    #### Front-End Technologies
    #### Back-End Technologies
4. Testing
    #### Manual Testing
    #### Validators
    #### Known Issues
5. Deployment
    #### Local Deploymeny
    #### Remote Depolyment
6. Credits
    #### Contents
    #### Code
    #### Acknowledgements
7. Disclaimer






## Features
### Existing Features
1. Navbar - Consists of the A Chefs Book logo which returns the user to the homepage of the app. There are also links to the “Home”, “View All”, “Add Recipe” and a “Search” bar 
2. View All - Constist of 2 main sections. The first section is a small intro which consist of an image and a search bar card. In the last section all recipes in the database are shown. Here the user can click on *View Recipe* to see the entire recipe. 
    - In the *View Recipe* the user is able to Edit or Delete a recipe
3. Add Recipe - In the add recipe the user is able to create his/her own recipe in the database. When the user submits the recipe he or she will see the recipe they just created
4. Search - The user able to search for recipes in different locations in the application. When the user search something he or she will be redirected to a result page which will show a card of a recipe that has ther term they searched for


### Future Features
* Create a sign-in forms, so that only user that are sign in can add, edit or remove recipes
* Create a path to store Cloudinary image to MonoDB
* The ability to change recipe images
* Create a new category in the application for dressings and sauces
* Adding a filter and sorting capabilities to the view all page
* Add time stamp and author to the recipes
* Hide sensitive information
* Link the quantities of ingredients in the recipes to the goods in stock
* Limit the ammount of recipes that are shown in *View All*, to work with page instead of a never ending page




## List of Technologies
### Front-End Technologies
* InVision
* Cloud9 IDE
* HTML
* CSS
* JavaScript
* Bootstrap
* Font Awesome
* Cloudinary
* Code Validators
* CSS Matic
* GitHub
 

### Back-End Technologies
* MongoDB
* Python
* Flask
* Heroku




## Testing

### Manual Testing
- This application was tested on desktop and mobile browsers to ensure cross compatibility and functionality.
- The application was tested to be responsive and to ensure it would be correctly displayed across all devices.
- I ensured that each one of the user stories were thoroughly tested to be functional without errors.
- The manual testing of the application covered the following:
    - When clicking on *View All* the user will be directed to the page showing all the recipes in the database
    - When the user clicks on *View Recipe* the user will be redirect to a page where the recipe will be visibile. And the user will have the option to *Edit* or *Delete* recipe
        - If the user clicks on *Edit* he/she will be redirected to the edit page
        - If the user clicks on *Delete* the user will recieve a confirmation request before the recipe is deleted
            - When and if the recipe is deleted the user will be redirected to the home page
    - When clicking on *Add Recipe* the user will be directed to the page when the user can created a new recipe
        - After clicking on the *Submit* button the user will be redirect to a page that shows the recipe that the user just added
    - The user has the capability to use the *Search Bar* on the Navbar or in the View All page. In both instances the user will be redirect the page that shows the results of the *search term*


### Validators
- HTML Validator: [Free Formatter](https://www.freeformatter.com/html-validator.html)
- CSS Validator: [CSS Lint](http://csslint.net/#results)
- JavaScript Validator: [Piliapp](https://www.piliapp.com/javascript-validator/)
- Python code was written according to [PEP8](https://www.python.org/dev/peps/pep-0008/)standards


### Known Issues

#### HTML Code
1. The use of crossorigin=anonymous in the script tag for Bootstrap
2. Attribute “for” not allowed on element “i” at this point.
3. Attribute “type” not allowed on element “textarea” at this point.
4. The “for” attribute of the “label” element must refer to a non-hidden form control
5. Validator is not recognize "{" or "}" tags used fror python script in the html

#### CSS code
1. The use of !important on line 21
2. Require fallback bordercolor for IE6, IE7 and IE8 on line 46
3. Using width with border can sometimes make elements larger than you expect on line 184

#### JavaScript code
1. The addition of the new line for the ingredients and instruction is very long. A solution would be to combine these function together as they are doing the same job
2. Sensitive information from Cloudinary is visable to everyone, this couls be rectified by writing a code that the user would have to insert his/her information to upload images to the cloud

#### Pyhton code
1. Sensitive information is visable to everyone, this can be rectified in de future by placing sensitive information in a .env file




## Deployment

This project had been build with [Cloud9 IDE](https://aws.amazon.com/cloud9/), [MongoDB](https://mongodb.com). For local deployment the code has been commited to Git and Pushed to [GitHub](https://github.com). And For remote deploment the code has been commited and pushed to [Heroku](https://heroku.com)

### Local Deployment
Please keep in mind that when running this project locally you have to install the following on your computer:
* [Cloud9 IDE](https://aws.amazon.com/cloud9/)
* [Python 3](https://www.python.org/) 
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [MongoDB](https://mongodb.com)
* [GitHub](https://github.com)

Following the next steps for local depoyment:
1. To clone the Github repository please do as following:
    - Under the repository name, click **Clone or Download**
    - In the Clone with HTTPs section, copy the clone URL
    - Open Git Bash
    - Change the working directory to where the cloned directory should be
    - Type **git clone**, and then paste the URL
    - Press **Enter** and the clone will be created
2. Navigate to the app.py file and replace *MONGO_URI* with your own key (Having you secret key public is not good practise)
3. Install the requirments from the *requirments.txt* file by:
    - sudo pip3 install -r requirements.txt
4. Sign up for a free account on MongoDB and create a new Database names All-recipes. The collections should be as following:

#### Categories (for dish type)
<img src="https://res.cloudinary.com/dbnahdjbc/image/upload/v1573334469/A%20Chefs%20Book/DB%20snips/dishtype_cdj11z.jpg"/>

#### difficulty (for recipe difficulty)
<img src="https://res.cloudinary.com/dbnahdjbc/image/upload/v1573334473/A%20Chefs%20Book/DB%20snips/difficulty_a6bn9d.png"/> 

#### recipes (for complete recipe information)
<img src="https://res.cloudinary.com/dbnahdjbc/image/upload/v1573334468/A%20Chefs%20Book/DB%20snips/recipes_lgps3c.png"/>

5. You should now be able to run you application locally be typing in your Cloud9 terminal
    - python3 app.py

6. To view view the application using cloud9 do the following steps:
    - Click *Preview* on the menubar, which opens a dropdown menu
    - In the dropdown menu click on *Preview Running Application*


### Remote Deployment
This application is currently deployed on [Heroku](insert link). To deploy this project to Heroku the following steps were taken:
1. Create a *requirements.txt* file so that Heroku can install the needed dependensies
    - sudo pip3 freeze --local > requirement.txt
2. Create a *Procfile* file so tell Heroku which application is being deployed and run
    - echo web: python app.py > Procfile
3. To start running you application after deployment you have to set the *dynos*
    - heroku ps:scale web=1
4. Sign up for a free Heroku account and create a new app. By clicking on *New* in the menubar and selecting *Create new app* in the dropdown menu.
5. Set the *Port* and *IP* in Heroku by doing the following steps:
    - In the *Settings* tab click on *Reveal Config Vars* button
    - Set the *KEY* and *VALUE* as following
        - KEY = IP ; VALUE = 0.0.0.0
        - KEY = PORT ; VALUE = 5000
6. For *Automatic Deployment* from GitHub follow the next steps:
    - In the *Deploy* tab Scroll down to *Apps connected to GitHub*
    - Search for your repository and click on *Connect* (keep in mind that you will need to give Heroku permission yo access your GitHub Repo)
    - After connection is made click on *Enable Automatic Deploys* in the Automatic Deploys section
    - Scroll down to Manual Deploy, choose the branch that you would like to deploy and click on *Deploy Branch*
7. Your application should be successfully deployed on Heroku




## Credits

The design idea for this webpage can from [All Recipes](https://www.allrecipes.com/)

### Contents
For the content of the webpage the following were used:
    - VectorStock
    - Favicon 
    - Made in a pinch
    - BBC Good Food 


### Code
I would like to give credits to the following:
    - Tim Nelson, I used your code as inspiration and for problem solving of my own code
    - Dave O'Dea, I used the code you have written for the addition of new input fiel for ingredients and instructions. Also your code was used for problem solving
    - Kevin Lesht, for the basic layout of one recipe
    - Material Design for Bootstrap, for providing me with the design of elements in my project
    - Start Bootrap, for providing me with the Navbar




### Acknowledgements
I would like to express my special thanks of gratitude to my mentor Mr. Rahul Lakhanpal, Tutor team of Code Institute and Slack Community. They helped and provided me with his/her valuable guidance.

Secondly, I would also like to thank my partner Chris Harms. For his deep interest and encouragement provided to me during the course of this project.




#### Disclaimer
The content of this web page is for educational purposes only.