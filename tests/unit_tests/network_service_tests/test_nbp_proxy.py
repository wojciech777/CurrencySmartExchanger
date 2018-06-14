import unittest

from network_service.nbp_service_proxy import NBPServiceProxy
from network_service.nbp_currency import NBPCurrency


class MockNBPService:
    lastMethod = ""

    def getCurrenciesCategoryA(self):
        self.lastMethod = "getCurrenciesCategoryA"
        return self.getCurrencies("test")

    def getCurrenciesCategoryB(self):
        self.lastMethod = "getCurrenciesCategoryB"
        return self.getCurrencies("test")

    def getCurrenciesCategoryC(self):
        self.lastMethod = "getCurrenciesCategoryC"
        return self.getCurrencies("test")

    def getCurrencies(self, category):
        models = [NBPCurrency("code", 0.2332, "currency")]
        return models


class NBPServiceProxyTestCase(unittest.TestCase):
    def test_get_categories(self):
        mock_nbp_service = MockNBPService()
        nbp_proxy = NBPServiceProxy()
        nbp_proxy.nbp_service = mock_nbp_service

        # Test Methods
        _ = nbp_proxy.getCurrenciesCategoryA()
        self.assertEqual(mock_nbp_service.lastMethod, "getCurrenciesCategoryA")
        # Test Methods
        _ = nbp_proxy.getCurrenciesCategoryB()
        self.assertEqual(mock_nbp_service.lastMethod, "getCurrenciesCategoryB")
        # Test Methods
        models = nbp_proxy.getCurrenciesCategoryC()
        self.assertEqual(mock_nbp_service.lastMethod, "getCurrenciesCategoryC")

        # Test Models Count
        self.assertEqual(len(models), 1)

        # Test Model Actualizing
        first = models[0]
        self.assertEqual(first.get_code(), 'code')
        self.assertEqual(first.get_currency(), 'currency')
        self.assertEqual(first.get_mid(), 0.2332)


if __name__ == '__main__':
    unittest.main()
