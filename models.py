

from django.db import models

class UserLogin(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    login_time = models.DateTimeField(auto_now_add=True)

class Title(models.Model):
    user = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    title_text = models.CharField(max_length=200)
