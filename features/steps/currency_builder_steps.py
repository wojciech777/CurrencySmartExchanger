# -- FILE: features/steps/currency_builder_steps.py

from behave import given, when, then

from models.currency_builder import CurrencyBuilder


@given('empty builder')
def step_impl(context):
    context.builder = CurrencyBuilder()


@when('user adds new exchange rate twice')
def step_impl(context):
    context.builder.add_currency('USD', 3.32)
    context.builder.add_currency('USD', 2.56)


@then('previous exchange should get updated')
def step_impl(context):
    currency = context.builder.build()
    assert currency.get_related_currency_by_name('USD').get_value() == 2.56
