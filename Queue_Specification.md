From our original architecture:

*The build queue will be a simple in memory queue that the Application Server adds to on a post-recieve webhook from Github. It will store Build ids. It is accessible by the server and the worker threads.*

While technically a part of the Application Server (it exists in the same Thread), the Queue is important enough to warrant a full specification. A Queue will be an object in our code, which we will instantiate and set as a instance variable in our Application Server. We will use the Python Queue class for our Queue. This class provides the following methods:

Queue.empty()
    return True if the queue is empty, False otherwise

Queue.put(*item*)
    enqueues *item* onto the queue

Queue.get()
    dequeues the first item on the queue

These methods are the only necessary external interfaces for this component. The following requirements must be satisfied for the Queue:

* it must be able to tell a consumer whether it is empty
* it must be able to enqueue a new object
* it must be able to dequeue the first object in the queue
* it must be able to be accessed and updated across multiple threads
