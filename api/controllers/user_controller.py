
from django.http import JsonResponse
from api.services.user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def create_user(self, request):
        res = self.service.create_user(request)

        return res
    
    def get_all_users(self):
        users = self.service.get_all_users()
        
        return users