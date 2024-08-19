from api.models import Register
from api.serializers import RegisterSerializer
from datetime import date

class GetDailyRegisterUseCase:
    def __init__(self):
      pass
    
    def execute(self, request):
      today = date.today()
      register_id = request.query_params.get('id')
      
      if register_id:
          registers = Register.objects.filter(created_at__date=today, id=register_id)
      else:
          registers = Register.objects.filter(created_at__date=today)
      
      serializer = RegisterSerializer(registers, many=True)
      return serializer.data