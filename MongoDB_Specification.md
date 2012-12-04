# From the architecture:

We will use MongoDB as our database because it allows easy storage of non-relational 
object types and embedded objects, which is logical for the JSON format of build objects 
that get passed from Github.

To communicate with MongoDB, we will use a ORM called PyMongo. This will easily allow us 
to create, update, and retrieve Build objects, without dealing with messy SQL queries. 
This is how the Application Server and Worker Thread will communicate with the DB.

Because MongoDB is schemaless, we will also use MongoKit as a layer to enforce a schema 
and simplify some calls.

The database is used to store the builds (and eventually the results of the build). 
It interacts with the Application Server and the Worker Thread. When a new build is published, 
the Application Server takes the information from Github, creates a new Build object and persists 
it in the database. Then, after passing the Build.id to the Worker Thread, the Thread retrives 
the Build information, builds it, and updates the Build object with the build results. When a user 
wants to see a build history, the Application Server loads the neccessary Build objects from the 
Database and displays them in HTML on the front end.

# Details

[Our build objects are defined here](https://github.com/cs181f/project2/blob/master/Persisted_Objects.md).

We will be using [PyMongo](http://api.mongodb.org/python/current/) to communicate with the
database. PyMongo will provide all of the required interactions with the database. We will
also use [MongoKit](http://namlook.github.com/mongokit/) as an intermediate layer for schema 
control and some simplification.

From MongoKit:

* class Build(Document): this inherits the Document class provided by MongoKit and includes
    all of the schema control.
* to_json(self): translates a Build into valid JSON
* from_json(self): translates JSON into a Build object
* validate(self): checks that the object is following the schema
* find(self): gathers all builds
* find(self, key:value): gathers matching builds

Overloaded:
* __init__: in order to gain some extra functionality in the constructor
* save: while PyMongo returns the ID number after saving to the database,
    MongoKit does not. Therefore, we will be overloading the save method
    to call the MongoKit save method.

Others:
* update_with_results(self): handles updating after build attempts

# Some notes

MongoDB uses "BSON" to store its objects, which is a superset of JSON (all JSON objects are BSON
objects). This will greatly help the interactions between various components, as JSON is already
required due to the integration with GitHub.

MongoDB uses unicode. [See here](http://docs.python.org/2/howto/unicode.html)
for a discussion of using unicode with Python. This should cause little-to-no issues, however
it is good to know about because strings will look different when retrieved from the database.

There are no optimizations currently planned for the database.