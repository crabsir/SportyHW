# Test Plan 

## 0: Preconditions
To be albe to run these tests the following setup is required:
* A user with access to the betting page;
* User balance for this user that is between 10 and 200 EUR;

## 1: Verify that a user can view match list
* Priority: Critical.
* Risk Rationale: Being able to view the Match List is central to the betting page experience, 
and it sets up the way a user will interact the page further.
* Steps:
  1. Go to the betting page: https://qae-assignment-tau.vercel.app/?user-id={yourUserId};
  2. View Match List;
  3. Select the closest upcoming match, odds: `1`;
  4. Switch to odds `2` for the same match.
* Expected Result: 
  1. Verify that the betting page is opened;
  2. Verify that:
     * Match List displays upcoming football matches;
     * Each match shows:
       * Home team vs Away team;
       * Football league;
       * Kickoff date/time label;
       * Three selectable odds buttons: `1`, `X`, `2`;
  3. Verify that:
     * The `1` odds are selected;
     * The Bet Slip for the selected odds is displayed;
     * Bet Slip contains information related to the selected odds;
  4. Verify that:
     * The `2` odds are selected;
     * The Bet Slip information is updated with the `2` odds' values.


## 2: Verify that a user can place a bet
* Priority: Critical.
* Risk Rationale: Placing a bet is core functionality for the betting page. 
It should therefore be expected that it is thoroughly checked as it directly deals with balance and payouts. 
* Steps:
  1. Go to the betting page: https://qae-assignment-tau.vercel.app/?user-id={yourUserId};
  2. Select the closest upcoming match, odds: `1`;
  3. Input the 10 EUR stake into the bet slip;
  4. Confirm bet placement by clicking 'Place bet' button;
  5. Review the bet receipt.
* Expected Result: 
  1. Verify that the betting page is opened;
  2. Verify that the `1` odds are selected;
  3. Verify that the bet slip displays correct bet information, including event, stake, potential payout;
  4. Verify that the bet receipt pop up is shown; 
  5. Verify that the bet receipt displays correct bet information, including unique bet ID, event, stake, 
  potential payout, bet timestamp.


## 3: Verify that a user's stake cannot exceed their balance
* Priority: Critical
* Risk Rationale: The system should not allow the user to exceed their balance 
as this would present financial and regulatory risks.
* Steps:
  1. Go to the betting page: https://qae-assignment-tau.vercel.app/?user-id={yourUserId};
  2. Try to select any upcoming event and place a bet on any of its odds;
  3. Make sure that the bet stake is larger than the available user balance but smaller than 100 EUR.
* Expected Result: 
  1. Verify that the betting page is opened;
  2. Verify that the betting slip for the event is displayed;
  3. Verify that the user stake cannot exceed their available balance.


## 4: Verify that a user cannot place a bet on a past event
* Priority: High
* Risk Rationale: The system should not allow the user to bet on a past event since that would present a financial risk 
of paying out odds that are bigger than 1 on an event that has already been resolved.
* Steps
  1. Go to the betting page: https://qae-assignment-tau.vercel.app/?user-id={yourUserId};
  2. Try to select any past event and place a bet on any of its odds. 
* Expected Result
  1. Verify that the betting page is opened;
  2. Verify that betting on the past events is unavailable.


## 5: Verify that a user cannot input a stake lower than the minimum allowed
* Priority: High
* Risk Rationale: The system should have safeguards against exceeding minimum stake amount 
to keep in line with the business logic requirements.
* Steps:
  1. Go to the betting page: https://qae-assignment-tau.vercel.app/?user-id={yourUserId};
  2. Try to select any upcoming event and place a bet on any of its odds; 
  3. Make sure that the bet stake is smaller than 1 EUR.
* Expected Result: 
  1. Verify that the betting page is opened;
  2. Verify that the betting slip for the event is displayed;
  3. Verify that the user stake cannot be lower than the minimum allowed (1 EUR).


## 6: Verify that a user cannot input a stake higher than maximum allowed
* Priority: High
* Risk Rationale: The system should have safeguards against exceeding maximum stake amount 
to keep in line with the business logic requirements.
* Steps:
  1. Go to the betting page: https://qae-assignment-tau.vercel.app/?user-id={yourUserId};
  2. Try to select any upcoming event and place a bet on any of its odds; 
  3. Make sure that the bet stake is greater than 100 EUR.
* Expected Result:
  1. Verify that the betting page is opened;
  2. Verify that the betting slip for the event is displayed;
  3. Verify that the user stake cannot be higher than the maximum allowed (100 EUR).
