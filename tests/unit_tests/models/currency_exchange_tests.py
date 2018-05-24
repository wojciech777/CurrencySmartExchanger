import unittest

from models.currencies_exchange import CurrenciesExchange
from models.currency_builder import CurrencyBuilder


class TestCurrencyExchangeClassMethods(unittest.TestCase):

    def test_add_currency(self):
        exchange = CurrenciesExchange()
        builder = CurrencyBuilder()
        currency = builder.set_name('USD').add_currency('EUR', 1.45).build()
        exchange.add_currency(currency, 'USD')
        print(exchange.get_exchange_rate('USD', 'EUR'))
