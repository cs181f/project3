"""
The BuildQueue class is the in memory queue that WorkerThreads pull
Builds that need to be built from.

It inherits from the standard Python multithreaded Queue. Documentation
for that class can be found at:

http://docs.python.org/2/library/queue.html
"""

# Python stdlib requirements for Queue
import Queue
import datetime

# BuildQueue inherits from standard multithreaded Python Queue
class BuildQueue(Queue):

    """ Constructor for BuildQueue.
    Accepts a maxsize of the queue """
    def __init__(self, maxsize=0):
        # calls standard Queue constructor
        Queue.__init__(self, maxsize)

    """ PUBLIC: Check whether there are any builds in the queue """
    def has_builds(self):
        # return True or False

    """ PUBLIC: Get ID of next build """
    def next_build(self):
        # returns Build ID of next Build in the queue

    """ PUBLIC: Add a build to the BuildQueue """
    def add_build(self, build):
        # returns boolean of whether build was successfully added