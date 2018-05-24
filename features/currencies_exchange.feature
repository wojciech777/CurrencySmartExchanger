# -- FILE: features/currency_exchange.feature

Feature: Creating a currency system allowing to check current exchange rates
  This feature allows user to use system to check
  exchange rates of given currencies

  Scenario: Adding system information from CSV file
    Given empty system
    When we import data from CSV file
    Then system should allow us to check exchange rates of added currencies