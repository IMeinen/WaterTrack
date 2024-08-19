from rest_framework import serializers
from api.models import User
from api.models import Register

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
      model = Register
      fields = '__all__'