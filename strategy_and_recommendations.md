## Strategy

This test framework is written using a Page Object Model approach. It utilizes PyTest fixtures, options, and markers
to create a robust and scalable solution for test automation.

The test scenarios that were selected for automation represent the highest priority test cases, which appear to have
an outsized effect on the feature as well as a major impact from a risk analysis perspective.

The main reason for leaving other tests manual is imposed task limitations. Due to the nature of its implementation
this framework is rather scalable, so the effort to expand it to the rest of the test scenarios should not be high.

## Recommendations

The main focus of the test cases that are automated is core bet placement functionality. This leaves
quite a lot of room for improvement in other areas, including but not limited to: filtering, error handling, 
negative scenarios.

Additional DB testing can be implemented, which is unfeasible currently due to the black box nature of the task.

Access to the data layer will also enable for faster data setup and verification, eliminating the need for workarounds 
that are in use presently.

In terms of CI/CD integration this framework can be integrated into the development pipeline for testing checks 
or be a standalone regression pipeline. Markers and options should be used as hooks for pipeline test management.
