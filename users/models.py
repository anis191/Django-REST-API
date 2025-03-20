from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

# To store user data, we use django built-in 'User' model by inheriting 'AbstractUser'
class User(AbstractUser):
    #At first we override(change) some User model field behavior:
    username = None #we don't need 'username' in our project.So we set 'username' to None
    email = models.EmailField(unique=True) #we need every user email unique, for authenticate

    # Add extra addition field in our User model: 
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # we did None the 'username', so now we need to tell the field of username alternative:
    USERNAME_FIELD = 'email' #that means we authenticate user with 'email', not 'username'.
    REQUIRED_FIELDS = [] #by default 'username' is required field in User model.So blank it.

    objects = CustomUserManager() #Details--> users > managers.py

    # Create a dunder methods for represent this model
    def __str__(self):
        return self.email
