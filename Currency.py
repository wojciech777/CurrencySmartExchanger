class Currency:
    def __init__(self,name,exchangeVector):
        self.name = name
        self.exchangeVector = exchangeVector

    def get_name(self):
        return self.name

    def get_exchangeVector(self):
        return self.exchangeVector
