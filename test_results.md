## Test Execution Results

| Test case ID and title                                    | Test result | Defect Reference | Notes                                                                                                   |
|-----------------------------------------------------------|-------------|------------------|---------------------------------------------------------------------------------------------------------|
| 1: Verify that a user can view match list                 | FAILED      | BUG-01           |                                                                                                         |
| 2: Verify that a user can place a bet                     | FAILED      | BUG-03           |                                                                                                         |
| 3: Verify that a user's stake cannot exceed their balance | PASSED      |                  | Test for a single bet placement passes but there are scenarios that allow user to exceed their balance. |

During additional exploratory testing the following defects were discovered:
* BUG-02
* BUG-04
* BUG-05

During test automation implementation the following defects were discovered:
* BUG-06
* BUG-07
