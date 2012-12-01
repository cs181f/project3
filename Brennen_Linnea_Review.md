#Build Design Review
It looks like this is a nearly complete implementation of the class, which is exciting in terms of the next step which will be to write it, but which does not fill all of the requirements of the design.

* The fields being used should be explained.
    - *Must Fix*
* self.from_json should have been explored and answered if it was being considered here
    - *Clarification*
* I don't understand what the 'unicode' keyword means.
    - *Clarification*
* All methods should be described, even if their implementations are fairly simple library calls.
    - *Must Fix*

#Build Test Plan Review
As we discussed there are a huge number of ways for this to fail that we need to be considering. The test plan does a good job of covering that important functionality expresses popular when the test suite is run, but a database in the wild is a fickle thing and we need to make sure that we are handling the error cases appropriately.

* Error Cases: Incomplete Write, Mislabeled fields, Invalid types for fields, etc. need to be tested
    - *Must Fix*
* What are we running test cases on? There is no setup of a test DB or teardown.
    - *Must Fix*
* There should be a black box test for inserting and updating, simply checking if the results are stored correctly.
    - *Must Fix*

#Verdict
I'm really glad there's as much implementation here as there is, but there needs to be more detail, as described in the Must Fix comments.