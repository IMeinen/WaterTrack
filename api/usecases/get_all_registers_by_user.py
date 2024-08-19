from api.models import Register
from django.db.models.functions import TruncDate
from django.db.models import Sum

class GetAllRegistersByUserUseCase:
  def __init__(self):
      pass
  
  def execute(self, request):
      user_id = request.query_params.get('user_id')
      registers = Register.objects.all()

      for register in registers:
          print(f"ID: {register.id}, User ID: {register.user_id}, Amount: {register.amount}, Created At: {register.created_at}")
      registers = Register.objects.filter(user_id=user_id).annotate(date=TruncDate('created_at')).values('date').annotate(total_amount=Sum('amount'))

      result = [{'date': register['date'], 'total_amount': register['total_amount']} for register in registers]
      return result