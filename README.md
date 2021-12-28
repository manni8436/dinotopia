# DINOTOPIA

![GitHub contributors](https://img.shields.io/github/contributors/manni8436/dinotopia)
![GitHub last commit](https://img.shields.io/github/last-commit/manni8436/dinotopia)
![GitHub language count](https://img.shields.io/github/languages/count/manni8436/dinotopia)
![GitHub top language](https://img.shields.io/github/languages/top/manni8436/dinotopia)

[Here is a link to the live final project]()

## INITIAL DESIGN

## FINAL DESIGN

![Final project image home page]()

## CONTENTS

* [User Experience](#user-experience)  
  * [User Stories](#user-stories)

* [Design](#design)
  * [Fonts](#fonts)
  * [Color Scheme](#color-scheme)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [Features Implemented](#features-implemented)
  * [Future Implementations](#future-implementations)

* [Database](#database)
  * [Database Schema](#database-schema)

* [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks And Libraries](#frameworks-and-libraries)
  * [Programs](#programs)

* [Deployment](#deployment)
  * [Initial Deployment](#initial-deployment)
  * [How To Fork A Repository](#how-to-fork-a-repository)
  * [How To Clone A Repository](#how-to-clone-a-repository)
  * [How To Make A Local Clone](#how-to-make-a-local-clone)

* [Testing](#testing)
  * [Code Validators](#code-validators)

* [Content](#content)
  * [Images](#images)
  * [Text Content](#text-content)

* [Acknowledgements](#acknowledgements)

[Back To Top](#dinotopia)

## USER EXPERIENCE

### USER STORIES

#### CLIENT GOALS

#### FIRST TIME VISITORS

#### RETURNING USER

[Back To Top](#dinotopia)

## DESIGN

### FONTS

### COLOR SCHEME

My overall colour scheme used throughout the site was the variety of colours in the image below.

![site colours]()

### WIREFRAMES

Wireframes were created using [Balsamiq](https://balsamiq.com/) and exported into a pdf format, which can be viewed [Here](add wireframes link here)

[Back To Top](#dinotopia)

## FEATURES

### FEATURES IMPLEMENTED

### FUTURE IMPLEMENTATIONS

[Back To Top](#dinotopia)

## DATABASE

### DATABASE SCHEMA

## TECHNOLOGIES

### LANGUAGES

<img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain-wordmark.svg" alt="HTML logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg" alt="CSS logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" alt="JavaScript logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python logo" width="50px" height="50px" /> 

## FRAMEWORKS AND LIBRARIES
<img src="https://github.com/devicons/devicon/blob/master/icons/bulma/bulma-plain.svg" alt="Bulma logo" width="50px" height="50px" /> <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" alt="Django logo" width="50px" height="50px" />

### PROGRAMS

<img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg" alt="Git logo" width="50px" height="50px" />

[Git](https://git-scm.com/) was used for version control by using the Gitpod terminal to add and commit to Git and push to Github.

#### GitPod

[GitPod](https://gitpod.io) was used as an IDE whilst coding this site.

#### GitHub

[GitHub](https://github.com/) is being used to store all the code for this project after being pushed from GitPod.

#### Am i Responsive

[Am i Responsive](http://ami.responsivedesign.is/) was used to create the image in my [Final Design](#final-design) section.

#### Firefox Developer Tools

[Firefox Developer](https://www.mozilla.org/en-GB/firefox/developer/) Tools was used for troubleshooting and trying new visual changes without it affecting the current code.

#### Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to ensure that the site was performing well, conforming to best practices, SEO and Accessibility guidelines.

[Favicon](https://favicon.io/) was used to create a favicon image that was added to the website.

#### Font Awesome

[Font Awesome](https://fontawesome.com/) was used for a few icons in the footer on all of this site's pages.

#### Google Fonts

[Google Fonts](https://fonts.google.com/) was used for all the text content on the site pages.

#### Balsamiq

[Balsamiq](https://balsamiq.com/) was used in the initial design process to make wireframes.

[Back To Top](#dinotopia)

#### jQuery

[jQuery](https://developer.mozilla.org/en-US/docs/Glossary/jQuery) was used to initialise Materialize CSS.

#### Flask

[Flask](https://palletsprojects.com/p/flask/) was used as the application framework.

#### Werkzeug

[Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/#) was used for user information protection.

#### PyMongo

[PyMongo](https://pymongo.readthedocs.io/en/stable/) was used to be able to work with MongoDB.

#### DNSPython

[DNSPython](https://www.dnspython.org/) was used as a toolkit to use with Python.

#### Flask-PyMongo

[Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/) was used to connect Python/Flask app to MongoDB.

#### Jinja

[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used to populate the site using the content from the site database.

[Back To Top](#dinotopia)

## SOLVED BUGS

[Back To Top](#dinotopia)

## TESTING

### CODE VALIDATORS

The W3C Markup Validator and W3C CSS Validator was used to validate my project to make sure there were no errors within the site.

* W3C CSS Validator Results

* JSHint
  * ![JavaScript]()

* PEP8 Online
  * ![PEP8]()

[Back To Top](#dinotopia)

### FULL TESTING

[Click Here](testing.md) to view the full testing steps that were completed on every device and browser.

### LIGHTHOUSE

### DESKTOP

#### Performance

#### Accessibility

#### Best Practices

#### SEO

## CONTENT

[Back To Top](#dinotopia)

## DEPLOYMENT

[Heroku](https://www.heroku.com/) was used to deploy the live site.

[Back To Top](#dinotopia)

### INITIAL DEPLOYMENT

This project was developed using [GitPod](https://gitpod.io) and pushed to [GitHub](https://github.com/) then was deployed using [Heroku](https://www.heroku.com/) using the following steps below:

1. Create a `requirements.txt` file using the command `pip3 freeze --local > requirements.txt` in the GitPod terminal.
2. Create a `Procfile` with the command `echo web: python app.py > Procfile`.
3. `git add .` and `git commit -m` the new requirements and Procfile files and then `git push` them to the GitHub repository.
4. Login or Sign up to [Heroku](https://www.heroku.com/).
5. Create a new app upon Login by clicking the "New" button in your dashboard. Choose a unique name and set the region to the one closest to you.
6. From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
7. Search for your GitHub repository and connect.
8. In the Heroku dashboard for the application, click on "settings" > "Reveal Config Vars".
9. Set the following config vars:

| Key | Value |
| ----------|--------- |
| PORT | 5000 |
| IP | 0.0.0.0 |
| DEBUG | False |
| MONGO_URI | USER_MONGODB_URI |
| MONGO_DBNAME | USER_MONGODB_NAME |
| SECRET_KEY | USER_SECRET_KEY |

[Back To Top](#dinotopia)

### HOW TO FORK A REPOSITORY

If you need to make a copy of a repository:

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [manni8436/dinotopia](manni8436/dinotopia).
3. In the top right corner, click "Fork".

### HOW TO CLONE A REPOSITORY

If you need to make a clone:

1. Login in to [GitHub](www.github.com).
2. Fork the repository manni8436/dinotopia using the steps above in [How To Fork a Repository](#HOW-TO-FORK-A-REPOSITORY).
3. Above the file list, click "Code".
4. Choose if you want to close using HTTPS, SSH or GitHub CLI, then click the copy button to the right.
5. Open Git Bash.
6. Change the directory to where you want your clone to go.
7. Type `git clone` and then paste the URL you copied in step 4.
8. Press Enter to create your clone.

[Back To Top](#dinotopia)

### HOW TO MAKE A LOCAL CLONE

If you need to make a local clone:

1. Login in to [GitHub](www.github.com).
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should close the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone` and then paste the URL you copied in step 4.
8. Press Enter, and your local clone will be created.

[Back To Top](#dinotopia)

### IMAGES

[Back To Top](#dinotopia)

### TEXT CONTENT

[Back To Top](#dinotopia)

### Code Credit

## ACKNOWLEDGEMENTS

[Back To Top](#dinotopia)