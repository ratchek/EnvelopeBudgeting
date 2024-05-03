
Check if API follows specs in docs
- [ ] Make API follow docs in splitting the total amounts into dollars and cents
- [ ] Should the user field for envelopes even be a thing in the docs?



Check that permissions are properly configured:
    Check that a user cannot:
    - [x] List a different user's envelopes
    - [x] Create an envelope for a different user
    - [x] View a different user's envelope
    - [x] Update a different user's envelope
    - [x] Delete a different user's envelope

    - [x] List a different user's fills
    - [x] Create a fill for a different user
    - [x] View a different user's fill
    - [x] Update a different user's fill
    - [x] Delete a different user's fill

    - [x] List a different user's transactions
    - [x] Create a transaction for a different user
    - [x] View a different user's transaction
    - [x] Update a different user's transaction
    - [x] Delete a different user's transaction

- [x] Check that only authenticated users can access API


- [x] Allow user to create envelopes without passing the user id explicitly
- [ ] Modify docs and add tests to be in line with the above
- [ ] Delete basic authentication option from production settings
- [ ] Add JWT endpoints to documentation

- [ ] Pagination?
- [ ] Filtering?
