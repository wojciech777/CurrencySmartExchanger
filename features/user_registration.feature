# -- FILE: features/user_registration.feature

Feature: Allowing end-user to create
  account in the system for future access.

  Scenario: Creating new account
    Given No existing account with given details
    When user registers in the application
    Then new account should be created and saved in the database