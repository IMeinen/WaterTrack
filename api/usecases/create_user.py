from api.serializers import UserSerializer

class CreateUserUseCase:
    def __init__(self):
      pass
    
    def execute(self,request):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
      return serializer.data