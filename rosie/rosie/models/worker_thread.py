"""
The WorkerThread class builds Build objects that are in the BuildQueue
asynchronously to the Application Server.

"""

# Library requirements for the WorkerThread
import threading
from build import Build

# WorkerThread inherits from the Python stdlib threading.Thread class.
class WorkerThread(threading.Thread()):
    """Constructor for WorkerThread class"""
    def __init__(self, queue):
        # calls standard Thread constructor
        threading.Thread.__init__(self)
        # stores BuildQueue in private variable
        self.queue = queue

    def run(self):
        """ PUBLIC: Starts worker in new Thread """

    def retrieve_build(id):
        """ PRIVATE: Retrieves build given build.ID """

    def build(build):
        """ PRIVATE: Builds build """

    def save_build_results(results):
        """ PRIVATE: stores build results in MongoDB """

    def post_to_github(results):
        """ PRIVATE: posts build results to Github """