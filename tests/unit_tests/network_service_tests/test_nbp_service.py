import unittest
import json

from network_service.nbp_service import NBPService


class MockResponce:
    def __init__(self, raw_string):
        self.raw_string = raw_string

    def json(self):
        return json.loads(self.raw_string)


class MockRequestService:
    urlMethod = ""
    mock_response_text = "[{\"table\": \"A\", \"no\": \"113/A/NBP/2018\", \"effectiveDate\": \"2018-06-13\", " \
                         "\"rates\": [" \
                         "{\"currency\": \"bat (Tajlandia)\", \"code\": \"THB\", \"mid\": 0.1133}, " \
                         "{\"currency\": \"dolar amerykański\", \"code\": \"USD\", \"mid\": 3.6461}, " \
                         "{\"currency\": \"dolar australijski\", \"code\": \"AUD\", \"mid\": 2.7625}, " \
                         "{\"currency\": \"dolar Hongkongu\", \"code\": \"HKD\", \"mid\": 0.4646}]}] "

    def get(self, url):
        self.urlMethod = url
        response = MockResponce(self.mock_response_text)
        return response


class NBPServiceTestCase(unittest.TestCase):
    _testUrl = "http://api.nbp.pl/api/exchangerates/tables/"

    def test_get_category_a(self):
        mock_request_service = MockRequestService()
        nbp_service = NBPService()
        nbp_service.requestService = mock_request_service

        models = nbp_service.getCurrenciesCategoryA()
        # Test Url
        self.assertEqual(mock_request_service.urlMethod, self._testUrl + "a")

        # Test Models Count
        self.assertEqual(len(models), 4)

        # Test Model Actualizing
        first = models[0]
        self.assertEqual(first.get_code(), 'THB')
        self.assertEqual(first.get_currency(), 'bat (Tajlandia)')
        self.assertEqual(first.get_mid(), 0.1133)

    def test_get_category_b(self):
        mock_request_service = MockRequestService()
        nbp_service = NBPService()
        nbp_service.requestService = mock_request_service

        models = nbp_service.getCurrenciesCategoryB()
        # Test Url
        self.assertEqual(mock_request_service.urlMethod, self._testUrl + "b")

        # Test Models Count
        self.assertEqual(len(models), 4)

    def test_get_category_c(self):
        mock_request_service = MockRequestService()
        nbp_service = NBPService()
        nbp_service.requestService = mock_request_service

        models = nbp_service.getCurrenciesCategoryC()
        # Test Url
        self.assertEqual(mock_request_service.urlMethod, self._testUrl + "c")

        # Test Models Count
        self.assertEqual(len(models), 4)


if __name__ == '__main__':
    unittest.main()
