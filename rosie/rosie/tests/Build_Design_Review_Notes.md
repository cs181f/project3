Build Design and Test Plan Review
November 30th, 2012
Jesse, Linnea, and Brennen in attendance

# Build design review

The fields that you include in your schema should be explained
    -DEFECT
    -MUST FIX

Clarify what `unicode` is and provide link to documentation
    -DEFECT
    -MUST FIX

Explain all methods even if they are simple wrappers to library calls; provide documentation for library calls used in each method
    -DEFECT
    -MUST FIX

Either use `__init__` to create the Build object instead of `from_json` or give an adequate explanation for not doing so
    -DEFECT
    -MUST FIX

Clarify all variables and methods provided by mongokit and provide links to documenations
    -DEFECT
    -MUST FIX


# Test plan review

Add tests for cases where error behavior is possible. Possible situations include: incomplete write, mislabled fields, invalid types for fields, lost connection, and a variety of others. Be more complete.
    -DEFECT
    -MUST FIX

Clarify what setup of database and server is necessary
    -DEFECT
    -MUST FIX

Add black box tests for insert and updating and a few that cover basic mongokit functionality for posterity
    -DEFECT
    -MUST FIX

Fix confusing comment on line 28
    -DEFECT
    -MUST FIX

For each test, add what the specific assertion you are testing is rather than a general overview of the functionality
    -DEFECT
    -MUST FIX

# Conclusion

Requires another meeting.
