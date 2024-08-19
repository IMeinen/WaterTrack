from django.db import models
from django.utils import timezone

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
    created_at = models.DateTimeField(null=True, blank=True)
    amount = models.FloatField()  

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(Register, self).save(*args, **kwargs)