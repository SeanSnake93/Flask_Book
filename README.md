# Flask Book Project ~ Week 5

Welcome to my Git Hub,
I have made a small website that is used to create a user/account,
it will then allow you to add or remove films created to and from your collection.

## Contents

1. Planning
* User Stories
* ERD
* Risk Assesment
2. Creation
* Models
* Forms
* Routes
3. Expanding
* Remore SHH
* Jenkins
4. Testing
* Pytest
* Debuging
* Pytest Coverage
5. Reflection
* Areas to improve
* Areas to reflect positivly
6. File Structure

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



#### Routes

### Expanding
#### Remore SHH
#### Jenkins

### Testing
#### Pytest
#### Debuging
#### Pytest Coverage

### Reflection
#### Areas to improve
#### Areas to reflect positivly

### File structure

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