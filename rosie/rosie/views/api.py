"""
This module exposes all of the endpoints of the application programming 
interface which will be hit by the external parts of Rosie. This includes
GitHub's Webhooks, the web frontend, and the command line interface.

Each API route is either returning accessible information or saving it and
triggering events, so the complexity of each method is fairly low.
"""
from flask import jsonify

###GitHub Webhook###

@api.route('/build')
def build():
    #parses Github Webhooks data into builds
    #creates Build object and stores it in the database

###HTML Endpoints###

@api.route('/ping')
def ping():
    #checks whether the worker is processing a build or free
    #returns jsonify(status of server)

@api.route('/builds/<build_id>')
def get_build():
    #looks up the build by its id in the database
    #looks at the status of the build
    #returns jsonify(status of build)

@api.route('/builds')
def get_builds():
    #looks at the status of all builds in the db
    #returns jsonify(status of all builds)

@api.route('/settings')
def settings():
    #accepts settings changes 
    #modifies config file with appropriate changes

@api.route('/blame')
def blame():
    #in the database, there will be an object of broken commit ranks
    #when a build breaks, the worker will increment the counter of that
    #commit's author. 
    #This endpoint returns that list sorted with the highest number of broken
    #commits first.

@api.route('/builds/new')
def rebuild():
    #takes build ID as parameter
    #looks up a build by that ID
    #rebuilds build to see if it fails new tests
