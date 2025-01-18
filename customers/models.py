# customers/models.py
from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=100,default='default_username')
    email = models.EmailField(unique=True,default='default@example.com')
    password = models.CharField(max_length=255,default='default_password')

    def __str__(self):
        return self.username
