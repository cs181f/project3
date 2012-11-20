"""
The WorkerThread class builds Build objects that are in the BuildQueue
asynchronously to the Application Server.

The only data structure used in this class is the BuildQueue class, which
we design in the build_queue.py file.
"""

# Library requirements for the WorkerThread
import threading # http://docs.python.org/2/library/threading.html
import requests # http://docs.python-requests.org/en/latest/
from build import Build

# WorkerThread inherits from the Python stdlib threading.Thread class.
class WorkerThread(threading.Thread()):
    """PUBLIC: Constructor for WorkerThread class"""
    def __init__(self, queue):
        # calls standard Thread constructor
        threading.Thread.__init__(self)

        # PRIVATE VARIABLES
        # stores BuildQueue in private variable
        self.queue = queue
        self.github_link = ''
        self.current_build

    def run(self):
        """ PUBLIC: Starts worker in new Thread """

    def read_configs(configs):
        """ PRIVATE: Reads configuration file to get Github link, etc """

    def retrieve_build(id):
        """ PRIVATE: Retrieves build given build.ID """

    def build(build):
        """ PRIVATE: Builds build """

    def save_build_results(results):
        """ PRIVATE: stores build results in MongoDB

        This method will be easily enabled by the Build object.
        """

    def post_to_github(results):
        """ PRIVATE: posts build results to Github

        This method will primarily be using the request module to communicate
        with the Github API.
        """