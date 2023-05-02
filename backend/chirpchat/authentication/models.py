from django.db import models

# Create your models here.
# Create your models here.
class auth_user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
