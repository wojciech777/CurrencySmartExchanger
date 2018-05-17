from models.Currency import Currency

class CurrencyBuilder:

    def __init__(self):
        self.currencyVector = []
        self.name = ""

    def set_name(self, name):
        self.name = name
        return self

    def add_currency(self, currency_name, added_currency_value_to_current_currency):
        for tup in self.currencyVector:
            if currency_name == tup[0]:
                self.currencyVector.remove(tup)
                break
        self.currencyVector.append((currency_name, added_currency_value_to_current_currency))
        return self

    def build(self):
        return Currency(self.name, self.currencyVector)
