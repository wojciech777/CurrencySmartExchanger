class NBPCurrency:
    def __init__(self, code, mid, currency):
        self._code = code
        self._mid = mid
        self._currency = currency

    def get_code(self):
        return self._code

    def get_mid(self):
        return self._mid

    def get_currency(self):
        return self._currency
