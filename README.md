FeaturePlus
============
Simple CRUD application to add new features to an existing app.

Tech Stack
----------
This project was built with the Django framework, for a full list of libraries/packages,
please see [requirements](https://github.com/inspaya/feature_plus/tree/develop/requirements)

Setup
-----
The project can be set up by:

* Installing [PostgreSQL](http://www.postgresql.org/download/linux/ubuntu/)
..* ```$ # Ubuntu/Debian Linux
..* ```$ apt-get install postgresql-9.3 postgresql-server-dev-9.3 libpq-dev```
..* ```$ # Mac
..* ```$ brew install postgresql```
* Installing [pip](http://pip.readthedocs.org/en/latest/installing.html)
* Creating a new [virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html)
with **pip** and cloning this project into that environment
..* ```$ virtualenv feature_plus```
..* ```$ cd feature_plus```
..* ```$ source bin/activate```
..* ```$ git clone https://github.com/inspaya/feature_plus.git```
* Installing requirements
..* ```$ cd feature_plus```
..* ```$ pip install -r requirements/local.txt```
* Exporting environment variables (the environment variables file will be emailed to you)
..* ```$ source .env```
* Setting up the Database (from the terminal, type) 
..* ```$ psql -d postgres < db_init.sql```
* Setting up the app (from the terminal type) 
..* ```$ ./manage.py migrate```


Testing
-------
You can execute the tests for this project by running 

..* ```$ ./manage.py test```

Coverage
--------
Code coverage is available by running

..* ```$ ./manage test_coverage```
