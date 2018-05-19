import unittest
from models.currency import Currency
from models.currency_name_value_pair import CurrencyNameValuePair

class CurrencyTests(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual("wojtek", Currency("wojtek", []).get_name())

    def test_get_name2(self):
        self.assertNotEqual("somethingElse", Currency("wojtek", []).get_name())

    def test_currency_with_null_name(self):
        self.assertNotEqual("", Currency(None, []).get_name())

    def test_currency_with_name_zero_length(self):
        self.assertEqual("", Currency("", []).get_name())

    def test_get_currencyVector(self):
        dictionary = [CurrencyNameValuePair("euro", 2), CurrencyNameValuePair("dollar", 3)]
        currency = Currency("", dictionary)
        self.assertEqual\
            (dictionary, currency.get_all_related_currencies_as_list())

    def test_get_specified_related_currency(self):
        dictionary = \
            [CurrencyNameValuePair("euro", 2),
             CurrencyNameValuePair("dollar", 3)]
        currency = Currency("", dictionary)
        self.assertEqual\
            (3,
             currency.get_related_currency_by_name("dollar")
             .get_value())


if __name__ == '__main__':
    unittest.main()
