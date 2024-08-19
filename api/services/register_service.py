from api.usecases.create_register import CreateRegisterUseCase
from api.usecases.get_daily_register import GetDailyRegisterUseCase

class RegisterService:
    def __init__(self):
        self.create_register_use_case = CreateRegisterUseCase()
        self.get_daily_register_use_case = GetDailyRegisterUseCase()
                
    def create_register(self, request):
        return self.create_register_use_case.execute(request)

    def get_daily(self, request):
        return self.get_daily_register_use_case.execute(request)
