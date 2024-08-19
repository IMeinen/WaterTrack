from api.models import Register
from datetime import date
from rest_framework.exceptions import ValidationError
from django.db.models import Sum
from api.usecases.get_goal_by_user import GetGoalByUserUseCase

class GetDailyRegisterUseCase:
    def __init__(self):
      self.getGoalByUserUseCase = GetGoalByUserUseCase()
    
    def execute(self, user_id , current_date = None):
      
      if not user_id:
        raise ValidationError("User ID is required.")

      if current_date is None:
        current_date = date.today()
      
      registers = Register.objects.filter(created_at__date=current_date, user_id=user_id)
      if not registers.exists():
          return {
              'user_id': user_id,
              'total_amount': 0,
              'current_date': current_date,
              'goal': 0,
              'reached_goal_percentage': 0
          }
      
      user_goal = self.getGoalByUserUseCase.execute(user_id)
      total_amount = registers.aggregate(total_amount=Sum('amount'))['total_amount']
      
      return {
          'user_id': user_id,
          'total_amount': total_amount,
          'current_date': current_date,
          'goal': user_goal['goal'],
          'reached_goal_percentage': round(total_amount * 100 / user_goal['goal'], 2)
      }