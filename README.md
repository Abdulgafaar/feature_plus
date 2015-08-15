FeaturePlus
============
Simple CRUD application to add new features to a seemingly existent app.

Tech Stack
----------
The following core Python packages/libraries were used:
* dj-database-url==0.3.0
* Django==1.8
* django-grappelli==2.7.1
* lettuce==0.2.20
* mock==1.0.1
* unittest2==1.1.0

Setup
-----
The project can be set up by:
* Installing requirements:
..*  ```sudo pip install -r requirements/base.txt```
* Exporting environment variables: 
..* ```export DATABASE_URL=postgres://testuser:pAssw0rd@localhost:5432/db_features```
* Setting up the Database (from the terminal, type): 
..* ```psql -d postgres < db_init.sql```
* Setting up the app (from the terminal type):
..* ```./manage.py migrate```
