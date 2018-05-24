class Currency:
    def __init__(self, name, exchange_dictionary):
        self._name = name
        self._exchange_dictionary = exchange_dictionary

    def get_name(self):
        return self._name

    def get_all_related_currencies_as_list(self):
        return self._exchange_dictionary

    def get_related_currency_by_name(self, currency_name):
        for currency_pair in self._exchange_dictionary:
            if currency_pair.get_name() == currency_name:
                return currency_pair
        return None
