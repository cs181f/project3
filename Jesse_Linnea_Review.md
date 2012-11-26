# Build Design Review

Judging from my experience with MongoKit and MongoDB, it looks like you've mostly implemented the class. That being said, the design is lacking necessary details to see what is actually going on. Some key thoughts:

* Where are your explanations for different variables?
    - *MUST FIX*
    - What is a Document or a Collection?

    - What do the __collection__ and __database__ variables do?
    - What are the dot_notation variables?
* What is the justification for the required fields and structure?
    - *MUST FIX*
* What is the purpose of the `to_json` method? When do we use that?
    - *MUST FIX*
* You say 'all others use mongokit or pymongo calls'. What are 'all others'?
    - *MUST FIX*
* Your explanation of what the fill method actually does is pretty convoluded.
    - *CLARIFICATION*
* What does the `@connection.register` method do?
    - *MUST FIX*
* What is the `unicode` value?
    - *MUST FIX*
* Can you link to documentation for the used mongokit functions?
    - *MUST FIX*
    - `self.get_from_id`
    - `self.to_json`
    - etc

# Test Plan Review

I understand that a lot of functionality for this class is implemented by mongokit, but I think you overlook a fair number of tests/scenarios. Overall, I think we need more tests. Some general thoughts:

* Confusing comment on line 28--don't seem to do what you say you do.
    - *MUST FIX*
* You only test the success cases...? What happens if things fail? We definitely need to test that the correct behavior occurs in failing situations.
    - *MUST FIX*
* How do you handle DB setup and teardown? There's no mention of that.
    - *MUST FIX*
* Are there really no black box tests? I find that a little hard to believe--shouldn't you test that validation occurs at least?
    - *MUST FIX*
* You have no information on the *specific* assertions that will be tested.
    - *MUST FIX*

Overall, I think that a lot more detail needs to be added to both the test plan and the design (although, for the design it's mainly just explanations of what's going on). Both are a good start, but they need work.

# VERDICT

All the must fix issues must be fixed before we can move forward.