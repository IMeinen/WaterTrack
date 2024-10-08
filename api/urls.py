from django.urls import path
from api.views import get_all_users, create_user, create_register, get_all_registers_by_user

urlpatterns = [
    path('user/create/', create_user),
    path('user/get-all/', get_all_users),
    path('register/create/', create_register),
    path('register/get-all-by-user/', get_all_registers_by_user),
]