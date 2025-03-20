'''
Why this managers.py?
=> When we try to create a superuser, django give a error. Because we change the behavior of built-in 'User' model fields. specially when change/override any field which is directly uses for authentication(username), in this case we need to customize the 'Manager' behavior.
'''
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    #First we override the create_user() method for normal user register
    def create_user(self, email, password=None, **extra_fields):
        #If user try register without email, we return with a error message
        if not email:
            raise ValueError('This Email Field Must Be Set!')
        email = self.normalize_email(email) #It's a good practice to write the email inside 'normalize_email()'.It hepls efficient searching the email in database.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) #Save the user in database
        return user
    
    #First we override the create_user() method for superuser user register
    def create_superuser(self, email, password=None, **extra_fields):
        #By default a super user staff is always true & also have all access permission:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        #We need to check this validation:
        if not extra_fields.get('is_staff'):
            raise ValueError('Super user must have is_staff=True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Super user must have is_superuser=True')
        
        #A superuser also have email,password etc. So call create_user() for that:
        return self.create_user(email, password, **extra_fields)