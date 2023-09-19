from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser,related_name='userprofile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    blog_logo = models.ImageField(upload_to='profile_picture', null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
