from flask import jsonify

###GitHub Webhook###

@api.route('/build')
def build():
    #parses Github Webhooks data

@api.route('/ping')
def ping():
    #returns jsonify(status of server)

###HTML Endpoints###

@api.route('/builds/<build_id>')
def get_build():
    #returns jsonify(status of build)

@api.route('/builds')
def get_builds():
    #returns jsonify(status of all builds)

@api.route('/settings')
def settings():
    #accepts settings changes 

@api.route('/blame')
def blame():
    #returns authors ranked by broken commits

@api.route('/builds/new')
def rebuild():
    #takes build ID as parameter
    #rebuilds build to see if it fails new tests
