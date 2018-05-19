from typing import List

from models import CurrencyNameValuePair


class Currency:
    def __init__(self, name, exchange_dictionary):
        self.name = name
        self.exchange_dictionary = exchange_dictionary

    def get_name(self):
        return self.name

    def get_all_related_currencies_as_list(self):
        return self.exchange_dictionary

    def get_related_currency_by_name(self, currency_name):
        for currency_pair in self.exchange_dictionary:
            if currency_pair.get_name() == currency_name:
                return currency_pair
        return None
