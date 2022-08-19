## Introduction

This Project contains REST endpoint API containing Places details.  This Enpoint internally prepares data from the API - https://storage.googleapis.com/coding-session-rest-api/{place_id} for a given place id.

Two valid place ids are: GXvPAor1ifNfpF0U5PTG0w and ohGSnJtMIC5nPfYRi_HTAg

This project is deployed currently using heroku and is live at
https://business-places-directory.herokuapp.com

## API endpoints 
* https://business-places-directory.herokuapp.com/places/GXvPAor1ifNfpF0U5PTG0w


## Create a development environment

### Requirements
To install and run this application you need:

* Python 2.7 or 3.3+
* virtualenv 
* git 

### Installation
The commands below install the application and its dependencies:

$ git clone https://github.com/kethzigilbert/business-places-directory.git
$ cd business-places-directory
$ virtualenv venv
$ . venv/bin/activate
(venv) pip install -r requirements.txt

### Running

(venv) $ python app.py