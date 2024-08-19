from api.models import User
from api.serializers import UserSerializer

class GetAllUsersUseCase:
    def __init__(self):
      pass
    
    def execute(self):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return serializer.data