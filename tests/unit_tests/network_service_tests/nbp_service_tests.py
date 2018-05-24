import unittest
import responses

from network_service.nbp_service_proxy import NBPServiceProxy


class NBPServiceTestCase(unittest.TestCase):
    def test_success_response(self):
        nbp_service = NBPServiceProxy()

        responses.add(responses.GET, 'http://api.nbp.pl/api/exchangerates/tables/a',
                      json={'error': 'not found'}, status=404)

        models = nbp_service.getCurrenciesCategoryA()
        self.assertEqual(len(models), 35)
        first = models[0]
        self.assertEqual(first.code, 'THB')
        self.assertEqual(first.currency, 'bat (Tajlandia)')


if __name__ == '__main__':
    unittest.main()
