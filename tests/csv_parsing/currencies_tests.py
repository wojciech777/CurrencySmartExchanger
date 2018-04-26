import unittest
import csv_parsing.currencies as currencies
import mock


class CurrenciesTestCase(unittest.TestCase):
    TEST_CSV_CONTENT = """,usd,eur,pln
usd,1,1.5,0.2765
eur,0.765,1,0.2451
pln,3.4235,4.324,1"""

    def test_filling_from_file(self):
        curr = self.__read_from_mock_file()
        value_list = list(curr.get_currencies_names())

        self.assertListEqual(value_list, ['usd', 'eur', 'pln'])

    def test_creating_currencies_list(self):
        curr = self.__read_from_mock_file()
        currencies = curr.get_currencies_list()
        self.assertTrue(currencies)

    def test_exchange_calculation(self):
        curr = self.__read_from_mock_file()
        curr.get_exchange_ratio('PLN', 'USD')

    def __read_from_mock_file(self):
        with mock.patch("builtins.open", mock.mock_open(read_data=self.TEST_CSV_CONTENT)) as mock_file:
            mock_file.return_value.__iter__ = lambda file: iter(file.readline, '')
            curr = currencies.CsvCurrencyExchange()
            curr.fill_data_from_csv('path/to/open', ',')
            return curr


if __name__ == '__main__':
    unittest.main()
