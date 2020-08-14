from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,null = False, on_delete =models.CASCADE)
    phno = models.IntegerField(max_length=10,blank=False)
    def __str__(self):
        return self.user.username
    

