# Create your models here.
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
from datetime import timedelta

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tournament_id = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=128)


    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # Hash password before saving
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class Tournament(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    CATEGORY_CHOICES = [
        (1, '4'),
        (2, '8'),
        (3, '16'),
    ]
   
    number_of_members = models.IntegerField(
        choices=CATEGORY_CHOICES,default='4'
        )
    created_on = models.DateTimeField(auto_now_add=True)
    winner = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.id)