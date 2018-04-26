import unittest
from Currency import Currency
from CurrencyBuilder import CurrencyBuilder

class TestCurrencyClassMethods(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual("wojtek", Currency("wojtek", []).get_name())

    def test_get_name2(self):
        self.assertNotEqual("wujek", Currency("wojtek", []).get_name())

    def test_get_currencyVector(self):
        vector = [("euro",2),("dollar",3)]
        currency = Currency("",vector)
        self.assertEqual([("euro",2),("dollar",3)], currency.get_exchangeVector())

    # def test_builder1(self):
    #     self.assertEqual("wojtek", CurrencyBuilder.set_name("wojtek").add_currency((123,321,312)).build().get_name())

if __name__ == '__main__':
    unittest.main()