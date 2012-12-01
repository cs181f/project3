#Worker Thread Design Review
Your design looks like it covers all of the necessary methods that will be used to run the worker thread, and though the descriptions are short, I feel like I have a good idea of what each one does. 

However, the design lacks details about how the thread will run, what it's lifecycle will be like, and how it will communicate with the other parts of the applciation. 

* How is a new build triggered? Is it an action triggered by an event, or by a repeated check finding work? Where is that check or ping?
    - *Must fix*
* What does a build look like and how is it built? build(build) builds a build is not sufficient.
    - *Must fix*
* Does a worker thread ever die? What happens if multiple are started?
    - *Clarification*
* There is no mention of the connection to the database, how do you access builds? I would expect this to be in the initialization.
    - *Must fix*
* What is the request module?
    - *Clarification*

#Build Queue Design Review
The queue is a mostly self-explanatory data structure, but there are still a few points of information that I would like to see in this design.

* Where is a build removed from the queue? I assume that it is in the 'next_build' method, but that should be detailed.
    - *Must fix*
* What happens at the maximum size of the queue? How is this size set?
    - *Must fix*
* I would also like to see some information about the consistency of the queue. You mention several times that it is multithreaded without any detail about which methods cause inconsistency and at what point that is resolved.
    - *Must fix*

#Test Plan Review
The test suites were very thorough and complete, and covered every important case I considered. 

* Why are there no black box tests for the build queue? It seems that there are several pieces of functionality could be easily expressed through those tests.
    - *Clarification*

#Verdict
There are several must-fix issues which need to be resolved before this design can be approved. 