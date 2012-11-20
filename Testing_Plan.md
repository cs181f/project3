For our tests, we will be using the nose framework: https://nose.readthedocs.org/en/latest/index.html.

This framework provides the ability to run the tests. To write the tests, we will be using `unittest`:

http://docs.python.org/2/library/unittest.html

Each our test suites will subclass the `unittest.TestCase` class and implement the necessary methods, including:

    setUp
    tearDown

Each of our individual tests will be a method that follows the unittest.TestCase paradigm:

    def test_<name of test>

For a detailed test plan for each module, check the *_test.py files in the test/ directory.