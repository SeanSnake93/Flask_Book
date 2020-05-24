# Flask Book Project ~ Week 5

Welcome to my Git Hub,
I have made a small website that is used to create a user/account,
it will then allow you to add or remove films created to and from your collection.

## Contents

1. File Structure
2. Planning
* User Stories
* ERD
* Risk Assesment
3. Creation
* Models
* Forms
* Routes
4. Expanding
* Remore SHH
* Jenkins
5. Testing
* Pytest
* Debuging
* Pytest Coverage
6. Reflection
* Areas to improve
* Areas to reflect positivly
7. File Structure

### File structure

*Note: All file names are in Bold*

Project(Flask_Book/)
Flask_Book/application/
Flask_Book/application/**__init__.py**
Flask_Book/application/**forms.py**
Flask_Book/application/**models.py**
Flask_Book/application/**routes.py**
Flask_Book/application/static
Flask_Book/application/static/css
Flask_Book/application/static/css/**main.css**
Flask_Book/application/templates
Flask_Book/application/templates/**layout.html**
Flask_Book/application/templates/**home.html**
Flask_Book/application/templates/**about.html**
Flask_Book/application/templates/**register.html**
Flask_Book/application/templates/**login.html**
Flask_Book/application/templates/**account.html**
Flask_Book/application/templates/**catalogue.html**
Flask_Book/application/templates/**add_movie.html**
Flask_Book/application/templates/**edit_movie.html**
Flask_Book/application/templates/**collection.html**
Flask_Book/etc/
Flask_Book/etc/systemd
Flask_Book/etc/systemd/system
Flask_Book/etc/systemd/system/**flask.service**
Flask_Book/script/
Flask_Book/script/**installation.sh**
Flask_Book/tests/
Flask_Book/tests/**__init__.py**
Flask_Book/tests/**test_back_end.py**
Flask_Book/**requirments.txt**
Flask_Book/**app.py**
Flask_Book/**create.py**

### Planing

1. **User Stories** - [Trello](https://trello.com/b/8pRYkq58)
2. **ERD** (Entity Relationship Diagram)
3. **Risk Assesment**

#### User Stories

#### ERD

When Starting with my original ERD I was looking at making a forum using comments under it.
with a like or dislike, have the comments filtered by the highest rated.
This being the most liked comment being at the top.
This project idea was changed is it resembled to close to the design we made collectivly.

***Users*** Table
**id**, title, frist_name, last_name, email, password

***Forum_Post*** Table
**id**, title, content, posted_date, post_auther *(Users)*, likes, dislikes

***Comments*** Table
**id**, auther *(Users)*, posted, content, forum_id *(Forum_Post)*, likes, dislikes

With the Flask_Blog created I reviewed my original plan and chose to change it up completely.
this is where the idea changed into a marketing site, creating a table of films and allowing the user to add this to their collection.

With the time constraint i did not want to have to create tables that would hold loads of data. It needed to be scailed down to the minimal required.

Using the MoSCoW method in my Trello I narrowed it down to a project that would consist of 3 tables.

***Users*** Table *(None Marked)*
**id**, first_name, last_name, email, password

***Films*** Table
**id**, title, year, genre, director, age_rating, description, bar_code

***Collection*** Table
**id**, user_id *(Users)*, films_id *(Films)*

Unlike the original this has 2 tables (Users and Films) completely seperate form one another and are related though a single (Collection) table.

The relationship between the tables is **One~*Users* --> Many~*Collection* <-- One~*Films***

*How would i improve the relationship?*
I woild include a relationship between the *Films* and *Users* tables. The reason for this is so that directors could be included as a user and this would allow for the site to be easirly expanded with a directors table. This table then being used to filter out films they have been a part of and maybe this would allow for better interation between directors and movie enthusists.

#### Risk Assesment

### Creation

#### Models

From the ERD I created 3 tables where made in total:-

Films Table
id ----------- Integer **(Primary Key)**
title -------- String max(100)
year --------- Integer
age ---------- String max(100)
director ----- String max(100)
genre -------- String max(20)
formating ---- String max(10)
description -- String max(1000)
code --------- Integer
owners ------- **(Forien Key Relationship)**

Collection Table
id ----------- Integer **(Primary Key)**
user_id ------ **(Forien Key)**
films_id ----- **(Forien Key)**

Users Table#
id ----------- Integer **(Primary Key)**
email -------- String max(500)
password ----- String max(500)
first_name --- String max(30)
last_name ---- String max(30)
collection --- **(Forien Key Relationship)**

#### Forms

Some Forms are used for multiple purposes, FilmsForm is used for multiple reasons primaraly due to the repertition of its data fields. When the data required changes some fields could be hidden and have data entered automaticly or in the case of the user, new form many be required to specify the fields required.

All Forms must be filled to required standard before allowing the user to submit Read/Write/Update/Delete(s') to the DATABASE.

***FilmsForm***
title, year, genre, director, rating, description, format, bar code, *submit*

This creates a form for a visiting member to see in cataloge and when subscribed in the catalogue can add to their collection allowing the film data to be filtered through the catalogue web page (Example bellow). On the catalogue page you can edit existing entries or delete them. In the menu your able to Add new films to the DATABASE.
*Used for Read/Write/Update/Delete funtions to DATABASE*

*Example...*
**Gladiator** 2000 Drama
Ridley Scott *15*
A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.
123456789

***RegistrationForm***
email, password, confirm_password, first_name, last_name, *submit*

This Form is used to enrole a user onto the site. Only requesting a name and email and password. on here the password must match the confirmed befor it is encripted in pw_hash to be stored on the SQL DATABASE.
*Used for Write funtions to DATABASE*

***LoginForm***
email, password, remember, *submit*

This Form is used to scan the Users Database, once found with check to see is the password matches. If on sumbitting all is correct the user will be logged in and sent to the 'home' page. In addition the site will remove and display additional content on pages once logged in.
*Used for Read funtions to DATABASE*

***UpdateAccountForm***
first_name, last_name, email, *submit*

Using the 'account' link the user is able to edit thier data and/or delete their account. By doing so will also delete all films within their collection from the Collection table.
*Used for Read/Update/Delete funtions to DATABASE*

#### Routes

***Create Routes***

add_movie
*Using the FilmsForm will add field data to the Films Table. If all needs are met the user will be redirected to the 'home' page.*

add_collection
*If the user requests to add the movie to collection, the movie will be filtered within the users current collection. If the result of the search turns up no entries, the film will be added to the users collection and sent to the 'collection' page.*

***Read Routes***

catalogue
*When opening the 'catalogue' page all the films in the DATABASE will be displayed on the screen. On the page the buttons to edit/delete or add to collection are hidden untill the user signs in and creates and account.*

collection
*Filtering the films within the users collection, when entering the 'collection' page, only the films hosted within the users collection will be displayed.*

***Update Routes***

edit_movie
*Using the FilmForm this pulls data from the Films DATABASE that is filtered by a filmID containing its id. Applying the data to the fields in the 'edit_movie' page and applying any changes the user wishes to make.*

***Delete Routes***

delete
*When looking to delete a film from the Films tabel this will filter thought all Collection table\, looking for entries of this film in all user collections and deletes them before removing the film.*

remove_collection
*Allowing the user to remove films from their collection, this filters out the film in the Collection table that relates to the logged in user and deletes the DATABASE entry.*

***User CRUD Routes***

register
*If the user is already logged in they are directed to the 'home' page. If not then the RegistrationForm is used to collect data to be entered into the Users table.*

login
*If the user is already logged in they are directed to the 'home' page. If not then they will be requested to provide their email and password. If not logged in and visit a page that reqires the user to be logged on, the user is directed to thsi page.*

account
*Using the UpdateAccountForm this pulls data from the Users table and applys this to the fields on screen. This data can then be changed and updated.*

account_delete
*This using the Users id will filter out all films in their collection and delete them one by one. Once all are removed it will log the user out and delete their account.*

logout
*Clicking the Logout button on the menu will Log the user out of the site.*

### Expanding



#### Remote SHH

Using GCP a keygen was created using "" 

Visual Studio

#### Jenkins

sudo su

sudo systemctl status jenkins

sudo systemctl start jenkins

sudo systemctl restart jenkins

sudo systemctl start jenkins

### Testing



#### Pytest

pytest

#### Debuging

During my tests I wanted to ensure that duplicates could not be applied to a Users collection. Testing the site this was possible as it was simply checking to see if the entry created match any on the table. The issue with this is that due to it being provided a fresh id number it would never match another enry in the table. As a result I needed to filter the data differently.

*Before changes where made...*
----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
application/__init__.py      14      0   100%
application/forms.py         54      7    87%
application/models.py        33      3    91%
application/routes.py       139     45    68%
---------------------------------------------
TOTAL                       240     55    77%

Changing the process from checking for a matching entry to filtering the Collection tabel for entries matching the users id and then filtering it again by the films id. If the serch returns no results the film is added to the users collection and datas added to the Collection table.

#### Pytest Coverage

pytest --cov ./application

----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
application/__init__.py      14      0   100%
application/forms.py         41      4    90%
application/models.py        33      3    91%
application/routes.py       131     10    92%
---------------------------------------------
TOTAL                       219     17    92%

pytest --cov --cov=/application --cov-report=term-missing

### Reflection

#### Areas to improve

#### Areas to reflect positivly