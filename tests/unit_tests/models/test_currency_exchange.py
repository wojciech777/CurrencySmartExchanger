import unittest

from csv_parsing.csv_importer import CsvCurrenciesImporter
from models.currencies_exchange import CurrenciesExchange
from models.currency_builder import CurrencyBuilder


class TestCurrencyExchangeClassMethods(unittest.TestCase):

    def test_add_currency(self):
        exchange = CurrenciesExchange()
        builder = CurrencyBuilder()
        currency = builder.set_name('USD').add_currency('EUR', 1.45).build()
        exchange.add_currency(currency, 'USD')
        print(exchange.get_exchange_rate('USD', 'EUR'))

    def test_adding_csv_currencies(self):
        exchange = CurrenciesExchange()
        importer = CsvCurrenciesImporter()
        importer.fill_data_from_csv('../../../features/test_data/rates.csv', ',')
        currency_list = importer.get_currencies_list()
        exchange.add_currencies(currency_list, 'USD')
