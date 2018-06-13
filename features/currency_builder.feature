# -- FILE: features/currency_builder.feature

Feature: Creating new currency
  This feature allows us to create an instance
  of new currency with all the exchange rates and name
  chosen arbitrarily.

  Scenario: Duplication of exchange rate
    Given empty builder
    When user adds new exchange rate twice
    Then previous exchange should get updated