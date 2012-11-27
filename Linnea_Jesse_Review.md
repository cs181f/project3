##Build Queue

SHOULD FIX: Is there rationale for why we are using maxsize=0 (infinite)?
In other words, have we considered a maximum size for the build
queue, for whatever reason?

MUST FIX: Document that "build" in add_build is a build ID stored as a
string, not the entire build object itself, please.

##Build Queue Test

SHOULD FIX: No specific comments come to me, but some discussion on how
test_can_be_accessed_from_multiple_threads especially
will be implemented would be appreciated.

##Worker Thread

QUESTION: __init__: does it makes sense to pass in a queue without
passing in the github information?

MUST FIX: Does the worker thread know where the database is? When/where
will this information be stored, or is this expected to be
stored in the build wrapper class? (in which case I need to know!)

MUST FIX: It appears that build is intended to call several other
methods of the class - document how build will actually work,
specifically what functionality the build method is
intended to encompass.

QUESTION: Any discussion on the thread's destruction?

##Worker Thread Test

No comments.