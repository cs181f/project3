# API Design Review

In general, I think it is a good overview of the design. You give a clear explanation of what the module accomplishes and give good summaries of what each individual route is supposed to do.

That being said, I think it lacks the depth necessary for a real design. Some key confusing things are:

* what is the `@api` variable
    - *MUST FIX*
* what does the `.route` wrapper do?
    - *MUST FIX*
* how do these routes interact with the DB? Does there need to be a variable that contains a connection to the DB?
    - *MUST FIX*
* What is the 'object of broken commits' that we store in the database? There's no mention of that in our architecture--does that require additional architecture support?
    - *MUST FIX*
* In the 'builds' route, do we really return *all* the builds in the DB? What if there are thousands and thousands--would it be better to paginate?
    -*CLARIFICATION*
* In 'builds/new' you say that it takes a 'build ID as a parameter'--where is this paramter?
* What does the jsonify function do? Is there a link to the documentation?
    - *MUST FIX*
* Are there any private routines that will be used or will all logic be contained in the individual routes?
    - *CLARIFICATION*
* How will the webhook data be parsed? Are you using a library for this or are you writing the code by hand?
    - *MUST FIX*
* Are these routes GETs or POSTs? Are there some situations where you need both (settings, perhaps since you need to see and update the settings)?
    - *MUST FIX*
* You mention command line interface, but I see no routes for this?
    - *CLARIFICATION*
* It'd be nice to see the comments with nicer formatting (""" blocks perhaps).
    - *FEATURE*


# Test Plan Review

Once again, I think your design provides a strong overview of both what the whole test suite covers, and what each test focuses on, but I think more detail is necessary. Some key thoughts:

* Are there any whitebox tests? If not, where is your 'convincing proof' that there is no misbehavior not covered by acceptance testing?
    - *MUST FIX*
* It seems that you only verify the positive outcomes? Where are the tests to verify correct error handling?
    - *MUST FIX*
* For none of these tests do you explain how you will configure the server to test the necessary conditions?
    - *CLARIFICATION*
* Your 'assertions' are more descriptions of the correct behavior and less actual, testable assertions. Can you be more clear?
    - *CLARIFICATION*
* How are you cleaning up the database? Does it occur after every test? After the whole suite?
    - *MUST FIX*
* All in all, I don't think one test per route is sufficient to provide the kind of coverage necessary to provide value.
    - *CLARIFICATION*

In sum, the overarching concept design in both your test plan and design is strong, but the details just aren't there. For another person, without prior understanding of the architecture and code, to come and implement this design, there needs to be a lot more information.

# VERDICT

All must-fix issues must be fixed before we can move forward.