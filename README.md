Introduction?

## Table of Contents
1. UX
    #### User Stories
    #### Wireframes
2. Features
    #### Existing Features
    #### Future Features
3. List of technologies
    #### Front-End Technologies
    #### Back-End Technologies
4. Testing
    #### Validators
    #### Known Issues
5. Deployment
    #### Local deploymeny
    #### Remote depolyment
6. Credits
    #### Contents
    #### Code
    #### Acknowledgements
7. Disclaimer


## Deployment

This project had been build with [Cloud9 IDE](https://aws.amazon.com/cloud9/), [MongoDB](https://mongodb.com). For local deployment the code has been commited to Git and Pushed to [GitHub](https://github.com). And For remote deploment the code has been commited and pushed to [Heroku](https://heroku.com)

### Local deployment
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
2. Navigate to the app.py file and !!!!! Secret KEY
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


### Remote deployment
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
6. Your application should be successfully deployed on Heroku


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