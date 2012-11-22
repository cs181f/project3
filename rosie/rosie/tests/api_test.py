"""
Test cases for the API. In these test cases, we verify that the
API responds correctly to calls of all endpoints.
BLACKBOX TESTING:

    def test_api_builds():
    def test_api_pings():
    def test_api_build_status():
    def test_api_build_statuses():
    def test_api_accepts settings changes():
    def test_api_blame_list():
    def test_api_rebuilds():
"""


import unittest
from views import (
    API
)

class APITest(unittest.TestCase):
    """Test cases for API"""
    @classmethod
    def setUpClass(self):
        """ Nothing needs to be set up """

    def setUp(self):
        """ Create a build object to test with"""

    def tearDown(self):
        """ Nothing needs to be torn down """

    def test_api_builds():
        """ Verifies that build is run correctly. """

    def test_api_pings():
        """ Verifies that correct status is returned. """

    def test_api_build_status():
        """ Verifies that when a build is running, returns the status of that
        build and otherwise returns clear."""

    def test_api_build_statuses():
        """ Verifies that all build statuses are returned correctly. """

    def test_api_accepts settings changes():
        """ Verifies that settings changed pushed are reflected in the
        config file """

    def test_api_blame_list():
        """ Verifies that a properly ordered list is returned """

    def test_api_rebuilds():
        """ Verifies that a build is properly rerun with new tests """
    


