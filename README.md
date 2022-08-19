## Introduction

This Project contains REST API Endpoint containing Places details.  This endpoint calls the given API - https://storage.googleapis.com/coding-session-rest-api/{place_id} and prepares data for the Frontend.

Two valid place ids are: GXvPAor1ifNfpF0U5PTG0w and ohGSnJtMIC5nPfYRi_HTAg

This project is deployed currently using heroku and is live at
https://business-places-directory.herokuapp.com/places/GXvPAor1ifNfpF0U5PTG0w

## API endpoints 
* https://business-places-directory.herokuapp.com/places/GXvPAor1ifNfpF0U5PTG0w


## Create a development environment

### Requirements
To install and run this application you need:

* Python 2.7 or 3.3+
* venv for Python 3 or virtualenv for Python 2.
* git 

### Installation
The commands below install the application and its dependencies:

    $ git clone https://github.com/kethzigilbert/business-places-directory.git
    $ cd business-places-directory
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) pip install -r requirements.txt

 
### Running

(venv) $ flask run

Open [http://127.0.0.1:5000/places/GXvPAor1ifNfpF0U5PTG0w] to view it in your browser.
