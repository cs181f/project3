# Changes

* adds additional information on how multithreadedness of BuildQueue is enabled and functions

Responding to must fix defect in BuildQueue review on line 15.

* removes maxsize parameter from BuildQueue

There should be no maxsize for the BuildQueue, so having this optional parameter was confusing. Responding to defect in BuildQueue review on line 11

* clarifies that `BuildQueue.next_build()` removes next Build.id from BuildQueue

Responding to clarification request on line 7 of BuildQueue review

* add detailed parameter notes for all methods in both BuildQueue and WorkerThread

Responding to feedback that it was often confusing what parameters should be

* gave better overview of how WorkerThread is started and terminated in top of comment of WorkerThread

Responding to confusion over how WorkerThread is started and terminated on line 7 and 15 of WorkerThread review

* clarified that all database connections are handled by the Build object for WorkerThread

Responding to confusion on how database connection works on line 19 of WorkerThread review

* clarified that configuration object is created in Application Server and passed to WorkerThread

Responding to confusion on how configuration is read and managed on line 27 of WorkerThread review

* add more information on `requests` and `threading` libraries

Responding to feedback that it was unclear how these libraries worked

* adds specific detail on how Build is actually 'built'

Responding to feedback that it was unclear how Build was actually built on line 11 of WorkerThread review

* adds justification for why there are no black box tests for BuildQueue

Responding to questions in BuildQueue review about why there were no black box tests

* adds information on how multithreadedness test will be implemented for BuildQueue

Responding to request for clarification in BuildQueue review about how this test would be implemented
