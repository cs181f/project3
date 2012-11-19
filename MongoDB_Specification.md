# From the architecture:

We will use MongoDB as our database because it allows easy storage of non-relational 
object types and embedded objects, which is logical for the JSON format of build objects 
that get passed from Github.

To communicate with MongoDB, we will use a ORM called PyMongo. This will easily allow us 
to create, update, and retrieve Build objects, without dealing with messy SQL queries. 
This is how the Application Server and Worker Thread will communicate with the DB.

The database is used to store the builds (and eventually the results of the build). 
It interacts with the Application Server and the Worker Thread. When a new build is published, 
the Application Server takes the information from Github, creates a new Build object and persists 
it in the database. Then, after passing the Build.id to the Worker Thread, the Thread retrives 
the Build information, builds it, and updates the Build object with the build results. When a user 
wants to see a build history, the Application Server loads the neccessary Build objects from the 
Database and displays them in HTML on the front end.

# Details

[Our build objects are defined here](https://github.com/cs181f/project2/blob/master/Persisted_Objects.md).
MongoDB is schemaless, and will not ensure that objects match our expected build objects.

We will be using [PyMongo](http://api.mongodb.org/python/current/) to communicate with the
database. PyMongo will provide all of the required interactions with the database:

* [db.insert(myBuildObject)](http://api.mongodb.org/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert): inserts a new object into the database. When inserting a new object, PyMongo automatically adds an '_id' key-value pair to the object and returns it, which can handle the id string for the build object. We may also consider using generating ids in some other way. insert can take in a python collection of objects in order to insert multiple objects at once.
* [db.find_one({key: value})](http://api.mongodb.org/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one): returns the first object in the database found with a matching key-value pair. This is how we will retrieve build objects from the database, using the key "_id" and the value returned when the object was first inserted.
* [db.update({key: value}, {$set: {key: value}})](http://api.mongodb.org/python/current/api/pymongo/collection.html#pymongo.collection.Collection.update): finds objects which contain a matching key-value pair to the first input and sets some other key to the specified value. Other arguments are possible; see the documentation.

Some other functions that may be useful:

* [db.find({key: value})](http://api.mongodb.org/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find): same as find_one, but returns a Cursor object which means that we may iterate through multiple matches. May be useful to use.

However, insert, find_one, and update should cover all of our requirements.

# Some notes

MongoDB uses "BSON" to store its objects, which is a superset of JSON (all JSON objects are BSON
objects). This will greatly help the interactions between various components, as JSON is already
required due to the integration with GitHub.

MongoDB uses unicode. [See here](http://docs.python.org/2/howto/unicode.html)
for a discussion of using unicode with Python. This should cause little-to-no issues, however
it is good to know about because strings will look different when retrieved from the database.

There are no optimizations currently planned for the database.