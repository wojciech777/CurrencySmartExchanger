import unittest
from models.currency import Currency


class TestCurrencyClassMethods(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual("wojtek", Currency("wojtek", []).get_name())

    def test_get_name2(self):
        self.assertNotEqual("somethingElse", Currency("wojtek", []).get_name())

    def test_currency_with_null_name(self):
        self.assertNotEqual("", Currency(None, []).get_name())

    def test_currency_with_name_zero_length(self):
        self.assertNotEqual("", Currency(None, []).get_name())

    def test_get_currencyVector(self):
        vector = [("euro", 2), ("dollar", 3)]
        currency = Currency("", vector)
        self.assertEqual([("euro", 2), ("dollar", 3)], currency.get_exchange_vector())


if __name__ == '__main__':
    unittest.main()
