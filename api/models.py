from django.db import models

class User(models.Model):
    id= models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    weight = models.FloatField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Register(models.Model):
    id= models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()