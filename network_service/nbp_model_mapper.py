import json
from network_service.models.nbp_currency import NBPCurrency

class NBPModelMapper:
    def mapModels(self, json_data):
        try:
            rates = json_data[0]['rates']
            print(rates)
            models = []
            for rate in rates:
                models.append(NBPCurrency(rate['code'], rate['mid'], rate['currency']))

            print(models)
            return models
        except KeyError:
            return []