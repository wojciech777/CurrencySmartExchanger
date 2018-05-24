class CurrenciesExchange:

    def __init__(self):
        self.currencies = []
        self.currency_dictionary = {}

    def add_currency(self, new_currency, default_exchange_currency):
        for currency in self.currencies:
            if not self.currency_dictionary[default_exchange_currency, currency]:
                raise ValueError("This default_exchange_currency can't be used, chose another")

        self.currencies.append(new_currency.get_name())
        self.currency_dictionary[new_currency.get_name(), new_currency.get_name()] = 1
        unknown_currencies = []

        for exchange_rate in new_currency.get_all_related_currencies_as_list():
            if self.currencies.count(exchange_rate.get_name()) == 0:
                unknown_currencies.append(exchange_rate.get_name())

            self.currency_dictionary[
                new_currency.get_name(), exchange_rate.get_name()] = exchange_rate.get_value()
            self.currency_dictionary[
                exchange_rate.get_name(), new_currency.get_name()] = 1 / exchange_rate.get_value()

        for currency in self.currencies:
            if not self.currency_dictionary[new_currency.get_name(), currency]:
                self.currency_dictionary[new_currency.get_name(), currency] = self.currency_dictionary[
                                                                                  new_currency.get_name(), default_exchange_currency] * \
                                                                        self.currency_dictionary[
                                                                            default_exchange_currency, currency]
                self.currency_dictionary[currency, new_currency.get_name()] = 1 / self.currency_dictionary[
                    new_currency.get_name(), default_exchange_currency] * self.currency_dictionary[
                                                                            default_exchange_currency, currency]
        for unknown_currency in unknown_currencies:
            for currency in self.currencies:
                self.currency_dictionary[unknown_currency, unknown_currency] = 1
                if not self.currency_dictionary[unknown_currency, currency]:
                    self.currency_dictionary[new_currency.get_name(), currency] = self.currency_dictionary[
                                                                                unknown_currency, new_currency.get_name()] * \
                                                                            self.currency_dictionary[
                                                                                new_currency.get_name(), currency]
                    self.currency_dictionary[currency, new_currency.get_name()] = 1 / self.currency_dictionary[
                        unknown_currency, new_currency.get_name()] * self.currency_dictionary[new_currency.get_name(), currency]
        for unknown_currency in unknown_currencies:
            self.currencies.append(unknown_currency)

    def add_currencies(self, currencies, default_exchange_currency):
        for currency in currencies:
            self.add_currency(currency, default_exchange_currency)

    def get_exchange_rate(self, source_currency, destination_currency):
        return self.currency_dictionary[source_currency, destination_currency]

    def get_currency_exchange_dictionary(self):
        return self.currency_dictionary

