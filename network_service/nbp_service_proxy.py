from network_service.nbp_service_interface import NBPServiceInterface
from network_service.nbp_service import NBPService
from datetime import datetime

class NBPServiceProxy(NBPServiceInterface):
    def __init__(self):
    	self.___nbp_service = NBPService()
    def getCurrenciesCategoryA(self):
        time = datetime.now().timestamp()
        result = self.___nbp_service.getCurrenciesCategoryA()
        print('get currencies done in ' + str(datetime.now().timestamp() - time) + ' ms')
        return result

    def getCurrenciesCategoryB(self):
        time = datetime.now().timestamp()
        result = self.___nbp_service.getCurrenciesCategoryB()
        print('get currencies done in ' + str(datetime.now().timestamp() - time) + ' ms')
        return result

    def getCurrenciesCategoryC(self):
        time = datetime.now().timestamp()
        result = self.___nbp_service.getCurrenciesCategoryC()
        print('get currencies done in ' + str(datetime.now().timestamp() - time) + ' ms')
        return result

    def getCurrencies(self, category):
        time = datetime.now().timestamp()
        self._nbp_service.getCurrencies(category)
        print('get currencies done in ' + str(datetime.now().timestamp() - time) + ' ms')