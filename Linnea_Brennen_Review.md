Overall, the API looks like it contains everything it requires.
Most if not all of my comments are requests for clarifications
and implementation details, specifically those that may have
impact on the design of other components.

##API

MUST FIX: I'm presuming that @api.route is a decorator provided by
the jsonify import - PLEASE link to the documentation
and/or include a discussion for those of us who have
not worked with flask extensively!

MUST FIX: When/where does the API find out and remember where the 
database is?

MUST FIX: get_build: please document where the build id to
look up is coming from.

QUESTION: get_builds: does this get *all* builds in the database,
including old ones? Should there be more specific
build retrieval methods? Some way to filter them?

MUST FIX: Lines 43-45 discuss build objects containing data I wasn't
aware of. Is this part of the "text" that goes in the
"error" field? If so, then we're good, otherwise
we need to talk.

##API Tests

QUESTION: Any rationale for why there are no whitebox tests?

SHOULD FIX: Seems very sparse - only one build object? Should there
be input so that the tests can make multiple build objects
to test with (to check routing works, for example)?
What about the database connection etc?

MUST FIX: Probably missing _'s in line 46.

## Verdict: all issues must be fixed to continue!
