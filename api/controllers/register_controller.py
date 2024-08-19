from django.http import JsonResponse
from api.services.register_service import RegisterService

class RegisterController:
    def __init__(self):
        self.service = RegisterService()

    def create_register(self, request):
        res = self.service.create_register(request)

        return res
    
    def get_all_registers_by_user(self, request):
        res = self.service.get_all_registers_by_user(request)

        return res