from rest_framework.decorators import api_view, renderer_classes
from api.controllers.user_controller import UserController
from api.controllers.register_controller import RegisterController
from rest_framework.response import Response
from rest_framework import status

userController = UserController()
registerController = RegisterController()

@api_view(['GET'])
def get_all_users(request):
    res = userController.get_all_users()
    return Response({'users': res}, status=status.HTTP_200_OK)  

@api_view(['POST'])
def create_user(request):
    res = userController.create_user(request)
    
    return Response(res, status=status.HTTP_200_OK)  

@api_view(['POST'])
def create_register(request):
    res = registerController.create_register(request)
    
    return Response(res, status=status.HTTP_200_OK)  

@api_view(['GET'])
def get_daily_register(request):
    res = registerController.get_daily(request)
    
    return Response(res, status=status.HTTP_200_OK)  

@api_view(['GET'])
def get_all_registers_by_user(request):
    res = registerController.get_all_registers_by_user(request)
    
    return Response(res, status=status.HTTP_200_OK)  