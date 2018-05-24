import unittest
import responses

from network_service.nbp_service import NBPService

class NBPServiceTestCase(unittest.TestCase):
    def test_success_response(self):
        nbpService = NBPService()

        responses.add(responses.GET, 'http://api.nbp.pl/api/exchangerates/tables/a',
                      json={'error': 'not found'}, status=404)

        models = nbpService.getCurrenciesCategoryA()
        self.assertEqual(len(models), 35)
        first = models[0]
        self.assertEqual(first.code, 'THB')
        self.assertEqual(first.currency, 'bat (Tajlandia)')
