# Changes

## Build design

* Added comments explaining and linking to documentation about the database 
    connection (clarification request from review)
* Added comments explaining and documenting the Document class (the 
    database's schema) (clarification request from review)
* Fully included necessary methods provided by MongoKit and linked to
    relevent documentation (clarification request from review)
* Removed fill method entirely (error fix from reivew)
* Overloaded __init__ and save to perform the functionality we require
    for our particular set up (error fix from reivew)
* Fixed a bug in __init__ (bug uncovered when fixing an error from review)

## Build tests

* Added blackbox tests (error fix from reivew)
* Added dirty tests (error fix from review)
* Fixed copy-paste typo in a comment (feedback from review)
* Explicitly stated what to check for in tests (clarification request
    from review)
