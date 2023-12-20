from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , related_name='profile_user',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self) :
        return f'{self.user.username} profile'
    