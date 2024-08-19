from django.http import JsonResponse
from api.services.register_service import RegisterService

class RegisterController:
    def __init__(self):
        self.service = RegisterService()

    def create_register(self, request):
        res = self.service.create_register(request)

        return res
    
    def get_daily(self, request):
        res = self.service.get_daily(request)

        return res