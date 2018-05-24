# -- FILE: features/steps/currencies_exchange_steps.py

from behave import given, when, then

from csv_parsing.csv_importer import CsvCurrenciesImporter
from models.currencies_exchange import CurrenciesExchange


@given('empty system')
def step_impl(context):
    context.exchange = CurrenciesExchange()
    context.importer = CsvCurrenciesImporter()


@when('we import data from CSV file')
def step_impl(context):
    context.importer.fill_data_from_csv('features/test_data/rates.csv', ',')
    context.exchange.add_currencies(context.importer.get_currencies_list(), 'USD')


@then('system should allow us to check exchange rates of added currencies')
def step_impl(context):
    assert context.exchange.get_exchange_rate('USD', 'EUR') == 1.5
