from api.usecases.create_user import CreateUserUseCase
from api.usecases.get_all_users import GetAllUsersUseCase

class UserService:
    def __init__(self):
        self.create_user_use_case = CreateUserUseCase()
        self.get_all_users_use_case = GetAllUsersUseCase()
        
    def create_user(self, request):
        return self.create_user_use_case.execute(request)
    
    def get_all_users(self):
        return self.get_all_users_use_case.execute()