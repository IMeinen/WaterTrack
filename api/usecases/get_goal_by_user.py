from api.models import User

class GetGoalByUserUseCase:
    def __init__(self):
      pass
    
    def execute(self,user_id):
        user = User.objects.filter(id=user_id)
        
        res = { 'goal': user[0].weight * 35 }
        return res