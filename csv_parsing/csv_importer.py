import csv

from models.currency_builder import CurrencyBuilder


class CsvCurrenciesImporter:

    def __init__(self):
        self._currencies = {}
        self._exchanges = {}

    def fill_data_from_csv(self, csv_path, delimiter):
        self._currencies.clear()
        self._exchanges.clear()

        with open(csv_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            self.__fill_currency_types(reader)
            self.__fill_exchange_rates(reader)

    def get_currencies_names(self):
        return list(self._currencies.values())

    def get_exchange_ratio(self, from_currency, to_currency):
        return self._exchanges[from_currency.upper(), to_currency.upper()]

    def get_currencies_list(self):
        if not self._exchanges:
            raise Exception("Class not initialized")
        else:
            currencies_list = []
            for curr_code in list(self._currencies.values()):
                curr_list = list(self._currencies.values())
                curr_list.remove(curr_code)
                builder = CurrencyBuilder()
                builder.set_name(curr_code)
                for to_calculate in curr_list:
                    builder.add_currency(to_calculate, self.get_exchange_ratio(curr_code, to_calculate))
                currencies_list.append(builder.build())
            return currencies_list

    def __fill_currency_types(self, reader):
        header = next(reader)
        types = iter(header)
        next(types)  # skip first, empty cell
        current_col = 0
        for currency_code in types:
            self._currencies[current_col] = currency_code.upper()
            current_col += 1

    def __fill_exchange_rates(self, reader):
        for row in reader:
            current_col = 0
            currency = ''
            for col in row:
                if current_col == 0:
                    currency = col
                else:
                    self._exchanges[self._currencies[current_col - 1], currency.upper()] = float(col)
                current_col += 1
