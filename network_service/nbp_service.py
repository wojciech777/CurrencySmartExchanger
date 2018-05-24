import math
import sys
import requests

from network_service.nbp_model_mapper import NBPModelMapper
from network_service.nbp_service_interface import NBPServiceInterface


class NBPService(NBPServiceInterface):
    def __init__(self):
        super().__init__()
        self._mapper = NBPModelMapper()
        self._url = 'http://api.nbp.pl/api/exchangerates/tables/'

    def getCurrenciesCategoryA(self):
        return self.getCurrencies('a')

    def getCurrenciesCategoryB(self):
        return self.getCurrencies('b')

    def getCurrenciesCategoryC(self):
        return self.getCurrencies('c')

    def getCurrencies(self, category):
        temp_url = self._url + category
        resp = requests.get(temp_url)
        print(resp.json())
        return self._mapper.map_models(resp.json())
