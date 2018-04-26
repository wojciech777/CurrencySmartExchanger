from Currency import Currency


class CurrencyBuilder:

    def __init__(self):
        self.currencyVector = []
        self.name = ""

    def set_name(self,name):
        self.name = name
        return self

    def add_currency(self,currencyItem):
        for tup in self.currencyVector:
            if currencyItem[0] == tup[0]:
                tup[1] = currencyItem[1]
                return self
        self.currencyVector.append(currencyItem)
        return self

    def build(self):
        return Currency(self.name,self.currencyVector)
