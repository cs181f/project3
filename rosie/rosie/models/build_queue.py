# The BuildQueue class is the in memory queue that WorkerThreads pull
# Builds that need to be built from.
#
# It inherits from the standard Python multithreaded Queue.

# Python stdlib requirements for Queue
import Queue
import datetime

# BuildQueue inherit from standard multithreaded Python Queue
class BuildQueue(Queue):

    # constructor for queue takes a maxsize of the queue
    def __init__(self, maxsize=0):
        # calls standard Queue constructor
        Queue.__init__(self, maxsize)

    # check whether there are any builds in the queue
    def has_builds():
        # return True or False

    # get ID of next build
    def next_build():
        # returns Build ID of next Build in the queue

    # add a build to the BuildQueue
    def add_build(build):
        # returns boolean of whether build was successfully added