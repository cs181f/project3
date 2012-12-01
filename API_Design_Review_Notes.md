Review of API Design and API Test Plan
November 30th, 2012
Jesse, Linnea, Brennen in attendance

# Review of API Design

Clarify what `@api` and `@api.route` do and provide documentation and/or include a discussion for them.
    -DEFECT
    -MUST FIX

Clarify how the API connects and communicates with the database.
    -DEFECT
    -MUST FIX

For the `get_build()` route, clarify that the route takes a build_id parameter and discuss how that is passed from the url string to the method.
    -DEFECT
    -MUST FIX

Clarify that `get_builds()` returns all builds
    -DEFECT
    -MUST FIX

Remove reference to broken commit rankings.
    -DEFECT
    -MUST FIX

Clarify what the `jsonify` function does and include documentation.
    -DEFECT
    -MUST FIX

Clarify whether routes are GET or POST.
    -DEFECT
    -MUST FIX

Format comments with “”” blocks
    -ISSUE
    -COMMENT

# Test Plan review

Add rationale for why there are no whitebox tests
    -DEFECT
    -MUST FIX

Missing underscores on line 46
    -DEFECT
    -MUST FIX

Add additional complexity by storing more build objects before accessing them through the API
    -DEFECT
    -MUST FIX

Add tests for negative outcomes for all API routes
    -DEFECT
    -MUST FIX

Add server configuration and setup information
    -DEFECT
    -MUST FIX

Provide actual assertions rather than correct behavior assumptions
    -DEFECT
    -MUST FIX

Provide information for how DB is going to be cleaned/setup
    -DEFECT
    -MUST FIX

# Conclusion

Requires another meeting.