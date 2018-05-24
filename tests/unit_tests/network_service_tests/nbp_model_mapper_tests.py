import unittest
import json

from network_service.nbp_service import NBPModelMapper

class NBPServiceTestCase(unittest.TestCase):
    def test_success_map(self):
        nbpModelMapper = NBPModelMapper()

        json_data = '[{"table": "A","no": "099/A/NBP/2018","effectiveDate": "2018-05-23","rates": [{"currency": "dolar Hongkongu","code": "HKD","mid": 0.4674},{"currency": "dolar kanadyjski","code": "CAD","mid": 2.8498},{"currency": "dolar nowozelandzki","code": "NZD","mid": 2.5322}]}]'
        json_obj = json.loads(json_data)


        models = nbpModelMapper.mapModels(json_obj)
        self.assertEqual(len(models), 3)
        first = models[0]
        self.assertEqual(first.code, 'HKD')
        self.assertEqual(first.currency, 'dolar Hongkongu')
        self.assertEqual(first.mid, 0.4674)

    def test_fail_map(self):
        nbpModelMapper = NBPModelMapper()

        json_data = '[{"table": "A","no": "099/A/NBP/2018","effectiveDate": "2018-05-23"}]'
        json_obj = json.loads(json_data)

        models = nbpModelMapper.mapModels(json_obj)
        self.assertEqual(len(models), 0)