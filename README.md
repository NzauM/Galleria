## @Galleria
[https://github.com/NzauM/Galleria.git]<br>
Author
Nzau Mercy Waeni

Description
Galleria is an application that lets you view images from different photographers and artists in all categories.

Setup Instructions:
Requirements
1. Clone the repository
Clone the the repository by running

git clone https://github.com/NzauM/Galleria.git
or download a zip file of the project from github

Navigate to the project directory

cd Galleria
2. Create a virtual environment
Install Virtualenv

pip install virtualenv
To create a virtual environment named virtual, run

virtualenv virtual
To activate the virtual environment we just created, run

source virtual/bin/activate
3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress

 $ psql
Then run the following query to create a new database named picsgarage

# create database picsgarage
4.Install dependencies
To install the requirements from requirements.txt file,

pip install -r requirements.txt
5.Create Database migrations
Making migrations on postgres using django

python3 manage.py makemigrations garage
then run the command below;

python3 manage.py migrate
6.Run the app
To run the application on your development machine,

python3 manage.py runserver
Running Tests
To run tests;

python3 manage.py test
Technologies Used
Django
Python
Html
Css
Javascript
Bootstrap
User stories
As a user of the application I should be able to:

 View different photos that interest me.
 Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
 Search for different categories of photos. (ie. Travel, Food)
 Copy a link to the photo to share with my friends.
 View photos based on the location they were taken.
Bugs
There are no know bugs at the moment

License
License

MIT license © 2019 NzauM

Collaboration Information
Clone the repository
Make changes and write tests
Push changes to github
Create a pull request
Contacts
Reach me on:

Email: mercywaenu16@gmail.com

