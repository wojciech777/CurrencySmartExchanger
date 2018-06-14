# -- FILE: features/creating_cryptocurrency.feature

Feature: Creating new currency
  This feature allows us to create an instance
  of new currency with all the exchange rates and name
  chosen arbitrarily.

  Scenario: Creating cryptocurrency
    Given system with some currencies defined
    When user defines new name and exchange rates for existing currencies
    Then new currency is created and its exchange rates for undefined, existing currencies is calculated using given currency