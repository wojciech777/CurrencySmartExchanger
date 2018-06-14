import unittest

from csv_parsing.csv_importer import CsvCurrenciesImporter
from models.currencies_exchange import CurrenciesExchange
from models.currency_builder import CurrencyBuilder


class TestCurrencyExchangeClassMethods(unittest.TestCase):

    def test_add_currency(self):
        exchange = CurrenciesExchange()
        builder = CurrencyBuilder()
        currency = builder.set_name('USD').add_currency('EUR', 1.45).add_currency('JEN', 2).build()
        exchange.add_currency(currency, 'USD')
        self.assertEqual(exchange.get_exchange_rate('USD', 'EUR'), 1.45)
        self.assertEqual(exchange.get_exchange_rate('USD', 'JEN'), 2)
        self.assertEqual(exchange.get_exchange_rate('JEN', 'EUR'), 2.9)

    def test_add_currencies(self):
        exchange = CurrenciesExchange()
        builder = CurrencyBuilder()
        builder.set_name('USD')
        builder.add_currency('EUR', 1.45)
        currency = builder.build()
        exchange.add_currency(currency, 'USD')

        builder2 = CurrencyBuilder()
        builder2.set_name('JEN')
        builder2.add_currency('USD', 2).add_currency('PLN', 3)
        currency2 = builder2.build()
        exchange.add_currency(currency2, 'USD')

        self.assertEqual(exchange.get_exchange_rate('JEN', 'EUR'), 2.9)

    def test_get_currencies(self):
        exchange = CurrenciesExchange()

        builder = CurrencyBuilder()
        builder.set_name('USD')
        builder.add_currency('EUR', 1.45)
        currency = builder.build()
        exchange.add_currency(currency, 'USD')

        self.assertEqual(exchange.get_currencies_names(), ['USD', 'EUR'])

    def test_adding_csv_currencies(self):
        exchange = CurrenciesExchange()
        importer = CsvCurrenciesImporter()
        importer.fill_data_from_csv('../../../features/test_data/rates.csv', ',')
        currency_list = importer.get_currencies_list()
        exchange.add_currencies(currency_list, 'USD')
        rate = exchange.get_exchange_rate('USD', 'EUR')
        assert rate == 0.765
