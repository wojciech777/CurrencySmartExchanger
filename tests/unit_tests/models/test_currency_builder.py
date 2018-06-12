import unittest

from models.currency_builder import CurrencyBuilder


class CurrencyBuilderTests(unittest.TestCase):
    def test_get_name(self):
        name = CurrencyBuilder() \
            .set_name("wojtek") \
            .add_currency("www", 123) \
            .build() \
            .get_name()
        self.assertEqual("wojtek", name)

    def test_number_of_added_currencies(self):
        currency = CurrencyBuilder() \
            .add_currency("euro", 123) \
            .add_currency("dolar", 321) \
            .build()
        self.assertEqual(2, len(currency.get_all_related_currencies_as_list()))

    def test_overriding_of_identical_currencies_in_currencies_vector(self):
        currency = CurrencyBuilder() \
            .set_name("adam") \
            .set_name("wojtek") \
            .add_currency("euro", 123) \
            .add_currency("euro", 124) \
            .build()
        self.assertEqual(1, len(currency.get_all_related_currencies_as_list()))

    def test_overriding_of_identical_currencies_in_currencies_vector2(self):
        currency = CurrencyBuilder() \
            .set_name("adam") \
            .set_name("wojtek") \
            .add_currency("euro", 123) \
            .add_currency("euro", 124) \
            .build()
        self.assertEqual(124, currency.get_related_currency_by_name("euro").get_value())

    def test_case_sensitivity_in_currencies_name(self):
        currency = CurrencyBuilder() \
            .set_name("adam") \
            .set_name("wojtek") \
            .add_currency("euro", 123) \
            .add_currency("Euro", 124) \
            .build()
        self.assertEqual(123, currency.get_related_currency_by_name("euro").get_value())

    def test_name_changing(self):
        currency = CurrencyBuilder() \
            .set_name("adam") \
            .set_name("wojtek") \
            .add_currency("euro", 123) \
            .add_currency("euro", 124) \
            .build()
        self.assertEqual("wojtek", currency.get_name())

    def test_setting_same_name_twice(self):
        currency = CurrencyBuilder() \
            .set_name("wojtek") \
            .set_name("wojtek") \
            .add_currency("euro", 123) \
            .add_currency("euro", 124) \
            .build()
        self.assertEqual("wojtek", currency.get_name())

    def test_name_of_empty_currency(self):
        currency = CurrencyBuilder().build()
        self.assertEqual('', currency.get_name())

    def test_currencies_vector_of_empty_currency(self):
        currency = CurrencyBuilder().build()
        self.assertEqual([], currency.get_all_related_currencies_as_list())


if __name__ == '__main__':    unittest.main()

