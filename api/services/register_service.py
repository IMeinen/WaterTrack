from api.usecases.create_register import CreateRegisterUseCase
from api.usecases.get_all_registers_by_user import GetAllRegistersByUserUseCase

class RegisterService:
    def __init__(self):
        self.create_register_use_case = CreateRegisterUseCase()
        self.get_all_registers_by_user_use_case = GetAllRegistersByUserUseCase()
                
    def create_register(self, request):
        return self.create_register_use_case.execute(request)

    def get_all_registers_by_user(self, request):
        return self.get_all_registers_by_user_use_case.execute(request)
