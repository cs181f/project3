""" Build Objects
Using the mongokit to control schema and simplify operations
Essentially a nice wrapper to make things as easy as possible
http://namlook.github.com/mongokit/index.html
"""

from mongokit import Document, Connection

connection = Connection()

@connection.register
class Build(Document):
    __collection__ = 'build_coll'   # database structure! consider using these to track branches?
    __database__ = 'build_db'       # database structure! consider using these to track branches?
    use_dot_notation = True
    dot_notation_warning = True
    structure = {
        'repository': {
            'url': unicode,
            'name': unicode,
            'description': unicode },
        'url': unicode,
        'author': {
            'email': unicode,
            'name': unicode },
        'message': unicode,
        'timestamp': unicode,
        'ref': unicode,
        'status': IS(0,1,2),
        'error': unicode
    }
    required_fields = [
        'repository.url',
        'repository.name',
        'repository.description',
        'url',
        'author.email',
        'author.name',
        'message',
        'timestamp',
        'ref',
        'status',
        'error',
    ]
    
    #self.to_json() will work!
    
    def fill(self, info)
    # takes in JSON, fills in fields
    # can possibly use self.from_json?
    # calls self.validate()
    # DOES NOT call self.save, calls insert() from pymongo
    # api directly. this is so that we can get the ID which
    # will be returned to be stored in the build queue.
    
    # use self.get_from_id(id) to find a build
    
    def update_with_results(self, results):
    # updates fields
    # calls self.validate(), then self.save()
    
    # all others should use mongokit or pymongo calls
    
