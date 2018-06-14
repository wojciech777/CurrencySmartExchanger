from network_service.nbp_currency import NBPCurrency


class NBPModelMapper:
    def map_models(self, json_data):
        try:
            rates = json_data[0]['rates']
            models = []
            for rate in rates:
                models.append(NBPCurrency(rate['code'], rate['mid'], rate['currency']))

            return models
        except KeyError:
            return []
