From our original architecture:

*The worker thread builds the user's project in the background and then posts the results to Github and stores them in the DB. The worker is started by the server when a a Github web hook hits the build API route. There are two primary functionality cases for the worker: (1) it builds the build, persists the build results to the database, checks the queue, which is empty and then terminates; and (2) it builds the build, persists the build results to the database, checks the queue, which has build ids remaining, then builds the next one until the queue is empty. The Worker Thread is asynchronous to the Application Server; however, there is only ever one running at a time, so builds are built synchronously and in order.*

The Worker Thread will be a class in our code, which is instantiated and used inside the Application Server code. It will run in a seperate Thread from the Application Server and must have access to the Queue.

We will subclass the threading.Thread class included in the Python standard library to create the Worker Thread. It must support the following methods:

void WorkerThread.new(queue)
    creates a new Worker Thread and sets the queue as an instance variable

void WorkerThread.run()
    runs the Worker Thread in a seperate Thread from the one where this is called

The Worker Thread must fulfill the following requirements:

* must run in a seperate Thread from the thread it is called in
* must build all builds in the Queue object in succession
* must access builds using the Build ID from the MongoDB database
* must persist the results of every build in the appropriate Build object in the MongoDB database
* must update Github using the Github API with the appropriate build results