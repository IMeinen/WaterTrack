from api.serializers import RegisterSerializer

class CreateRegisterUseCase:
    def __init__(self):
      pass
    
    def execute(self,request):
      serializer = RegisterSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
      return serializer.data