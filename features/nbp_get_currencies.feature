# -- FILE: features/user_registration.feature

Feature: Allowing end-user to check
  actual currencies from NBP API.

  Scenario: Checking actual currencies
    Given Want to know actual bank currencies
    When Make request to server
    Then Check actual currencies