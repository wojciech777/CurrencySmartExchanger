class Currency:
    def __init__(self, name, exchange_vector):
        self.name = name
        self.exchange_vector = exchange_vector

    def get_name(self):
        return self.name

    def get_exchange_vector(self):
        return self.exchange_vector
