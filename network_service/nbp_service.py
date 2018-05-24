import math
import sys
import requests

from network_service.nbp_model_mapper import NBPModelMapper

class NBPService:
    def __init__(self):
        self._mapper = NBPModelMapper()
        self._url = 'http://api.nbp.pl/api/exchangerates/tables/'

    def getCurrenciesCategoryA(self):
        return self.getCurrencies('a')

    def getCurrenciesCategoryB(self):
        return self.getCurrencies('b')

    def getCurrenciesCategoryC(self):
        return self.getCurrencies('c')

    def getCurrencies(self, category):
        tempUrl = self._url + category
        resp = requests.get(tempUrl)
        print(resp.json())
        return self._mapper.mapModels(resp.json())
