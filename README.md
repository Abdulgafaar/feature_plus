FeaturePlus 
============
Simple CRUD application to add new features to an existing app.

Tech Stack
----------
This project was built with the Django framework, for a full list of libraries/packages,
please see [requirements](https://github.com/inspaya/feature_plus/tree/develop/requirements) files for details.

Setup
-----
The project can be set up by:
* Installing [PostgreSQL](http://www.postgresql.org/download/linux/ubuntu/) 
  * ```$ [sudo] brew install postgresql # Mac OS```
  * ```$ [sudo] apt-get install postgresql-9.3 postgresql-server-dev-9.3 libpq-dev # Ubuntu/Debian```
* Installing [pip](http://pip.readthedocs.org/en/latest/installing.html)
* Creating a new [virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html)
with **pip** and cloning this project into that environment
  * ```$ virtualenv feature_plus```
  * ```$ cd feature_plus```
  * ```$ source bin/activate```
  * ```$ git clone [Clone]( https://github.com/inspaya/feature_plus.git"click to clone")```
* Installing requirements
  * ```$ cd feature_plus```
  * ```$ [sudo] pip install -r requirements/local.txt```
* Exporting environment variables (the environment variables file will be emailed to you)
  * ```$ source .env```
* Setting up the Database via the postgres user (from the terminal, type)
  * ```$ psql -d postgres < db_init.sql```
* Setting up the app (i.e. creating tables) 
  * ```$ ./manage.py migrate```
* Launching the Django development server
  * ```$ ./manage.py runserver [port] # optionally specify a port, default is 8000```

Usage
-----
Type the address in a browser **http://localhost:8000/features/** (then replace 8000 with the port you specified
if you used a custom port)
* Adding a Feature: Use the form to add new features
* Editing a Feature: Click on the feature name to edit the feature
* Deleting a Feature: Click on the Delete link beside each feature

Testing
-------
You can execute the tests for this project by running 
  * ```$ ./manage.py test```

Coverage
--------
Code coverage is available (for ```app``` only) by running
  * ```$ ./manage test_coverage app```
