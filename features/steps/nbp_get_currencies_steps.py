# -- FILE: features/steps/nbp_get_currencies_steps.py

from behave import given, when, then

from network_service.nbp_service_proxy import NBPServiceProxy


@given('Want to know actual bank currencies')
def step_impl(context):
    context.nbp_service = NBPServiceProxy()


@when('Make request to server')
def step_impl(context):
    context.currencies = context.nbp_service.getCurrenciesCategoryA()


@then('Check actual currencies')
def step_impl(context):
    assert context.currencies
