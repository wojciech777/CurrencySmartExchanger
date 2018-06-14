from network_service.nbp_service_interface import NBPServiceInterface
from network_service.nbp_service import NBPService
from datetime import datetime


class NBPServiceProxy(NBPServiceInterface):
    def __init__(self):
        super().__init__()
        self.nbp_service = NBPService()

    def getCurrenciesCategoryA(self):
        time = datetime.now().timestamp()
        result = self.nbp_service.getCurrenciesCategoryA()
        print('get currencies done in ' + str(datetime.now().timestamp() - time) + ' ms')
        return result

    def getCurrenciesCategoryB(self):
        time = datetime.now().timestamp()
        result = self.nbp_service.getCurrenciesCategoryB()
        print('get currencies done in ' + str(datetime.now().timestamp() - time) + ' ms')
        return result

    def getCurrenciesCategoryC(self):
        time = datetime.now().timestamp()
        result = self.nbp_service.getCurrenciesCategoryC()
        print('get currencies done in ' + str(datetime.now().timestamp() - time) + ' ms')
        return result
