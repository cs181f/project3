"""
Test cases for the Build class. Since the Build object
is just an extension of mongokit's Document class and
implements very little on its own, we only need the
following tests:

WHITEBOX TESTING:

    def test_build_from_json
    def test_build_from_database
    def test_update_existing_build

"""

import unittest
from models import (
    Build
)


class WorkerThreadTest(unittest.TestCase):
    """Test cases for Worker Thread"""
    @classmethod
    def setUpClass(self):
        """ Nothing needs to be set up for the whole class """

    def setUp(self):
        """ Create a queue and worker thread """
        self.Build = Build()

    def tearDown(self):
        """ Nothing needs to be torn down """

    def test_build_from_json(self):
        """ Tests that sample JSON results in a valid Build object that is
            correctly inserted into the database """
    def test_build_from_database(self):
        """ Tests that Build objects are correctly retrieved from the
            database given an ID (as would be used by the BuildQueue) 
            This one is possibly unnecessary given that we will be
            using a mongokit function """
    
    def test_update_existing_build(self):
        """ Tests that updating a build with build results works correctly """
