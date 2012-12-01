Build Queue Design and Test Plan Review
November 30th, 2012
Jesse, Linnea, and Brennen in attendance

# Design review

Clarify how builds are removed from the queue
    -DEFECT
    -MUST FIX

Clarify that `maxsize=0` means that there is no max size
    -DEFECT
    -MUST FIX

Clarify how the multithreadedness of the build queue is navigated by the WorkerThread
    -DEFECT
    -MUST FIX

Clarify that `build` in `add_build` is just a string that represents the ID of the build rather than the whole build object
    -DEFECT
    -MUST FIX

# Test plan review

Add more detail on how `test_can_be_accessed_from_multiple_threads` will be implemented.
    -DEFECT
    -MUST FIX

Add black box tests for Build Queue
    -DEFECT
    -MUST FIX

# Conclusion

Requires another meeting.