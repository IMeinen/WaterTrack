from api.serializers import RegisterSerializer
from api.usecases.get_daily_register import GetDailyRegisterUseCase

class CreateRegisterUseCase:
    def __init__(self):
      self.get_daily_register_use_case = GetDailyRegisterUseCase()
    
    def execute(self,request):
      serializer = RegisterSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
      
      current_day_data = self.get_daily_register_use_case.execute(request.data['user_id'])

      return current_day_data