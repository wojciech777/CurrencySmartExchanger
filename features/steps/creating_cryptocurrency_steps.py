# -- FILE: features/steps/creating_cryptocurrency_steps.py

from behave import given, when, then

from models.currencies_exchange import CurrenciesExchange
from models.currency_builder import CurrencyBuilder


@given('system with some currencies defined')
def step_impl(context):
    builder = CurrencyBuilder()
    builder.set_name('USD')
    builder.add_currency('EUR', 0.75)
    context.exchange = CurrenciesExchange()
    context.exchange.add_currency(builder.build(), 'USD')


@when('user defines new name and exchange rates for existing currencies')
def step_impl(context):
    builder = CurrencyBuilder()
    builder.set_name('BTC')
    builder.add_currency('EUR', 5)
    currency = builder.build()
    context.exchange.add_currency(currency, 'EUR')


@then('new currency is created and its exchange rates for undefined, existing currencies '
      'is calculated using given currency')
def step_impl(context):
    expected_rate = 1 / 0.75 * 5
    actual_rate = context.exchange.get_exchange_rate('BTC', 'USD')
    assert actual_rate == expected_rate
