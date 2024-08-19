import pytest
from datetime import date
from api.models import Register
from api.usecases.get_daily_register import GetDailyRegisterUseCase
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_execute_without_user_id():
    use_case = GetDailyRegisterUseCase()
    with pytest.raises(ValidationError):
        use_case.execute(None)

@pytest.mark.django_db
def test_execute_no_registers(mocker):
    user = User.objects.create(username='testuser')
    use_case = GetDailyRegisterUseCase()
    
    mocker.patch('api.usecases.get_goal_by_user.GetGoalByUserUseCase.execute', return_value={'goal': 2000})
    
    result = use_case.execute(user.id, date.today())
    
    assert result == {
        'user_id': user.id,
        'total_amount': 0,
        'current_date': date.today(),
        'goal': 0,
        'reached_goal_percentage': 0
    }

@pytest.mark.django_db
def test_execute_with_registers(mocker):
    user = User.objects.create(username='testuser')
    Register.objects.create(user_id=user.id, amount=500, created_at=date.today())
    Register.objects.create(user_id=user.id, amount=1500, created_at=date.today())
    
    use_case = GetDailyRegisterUseCase()
    
    mocker.patch('api.usecases.get_goal_by_user.GetGoalByUserUseCase.execute', return_value={'goal': 2000})
    
    result = use_case.execute(user.id, date.today())
    
    assert result == {
        'user_id': user.id,
        'total_amount': 2000,
        'current_date': date.today(),
        'goal': 2000,
        'reached_goal_percentage': 100.00
    }