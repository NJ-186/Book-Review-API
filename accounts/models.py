from django.db import models

import jwt
from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from datetime import datetime
from django.utils.timezone import timedelta
import time
# Create your models here.

class UserManager(BaseUserManager):

    def get_by_natural_key(self, email):
        return self.get(email=email)
 
 
class AuthorManager(BaseUserManager):
 
    def create_author(self, first_name, last_name, email, bio, password=None, **extra_fields):
        
        if email is None:
            raise TypeError('Users must have an email address.')

        author = Author(first_name=first_name, last_name=last_name, 
                          email=self.normalize_email(email), bio=bio)
        
        author.set_password(password)
        author.save()
        return author
 
 
class NormalUserManager(BaseUserManager):
 
    def create_normaluser(self, first_name, last_name, email, profession, password=None, **extra_fields):

        if email is None:
            raise TypeError('Users must have an email address.')
        
        normal_user = NormalUser(first_name=first_name, last_name=last_name, 
                            email=self.normalize_email(email), profession=profession)

        normal_user.set_password(password)
        normal_user.save()
        return normal_user

        
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]
    
    objects = UserManager()
 
    @property
    def token(self):
        dt = datetime.now() + timedelta(days=20)
        token = jwt.encode({
            'id': self.email,
            'exp': int(time.mktime(dt.timetuple()))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')
 
    def get_full_name(self):
        return (self.first_name+' '+self.last_name)
 
    def get_short_name(self):
        return self.first_name
 
    def natural_key(self):
        return (self.first_name, self.last_name)
 
    def __str__(self):
        return self.email


class Author(User, PermissionsMixin):
    bio = models.CharField(db_index=True, max_length=255)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'bio']
 
    objects = AuthorManager()
 
    def __str__(self):
        return self.first_name


class NormalUser(User, PermissionsMixin):
    profession = models.CharField(db_index=True, max_length=255)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'profession']
 
    objects = NormalUserManager()
 
    def __str__(self):
        return self.first_name


class UserManager(BaseUserManager):

    def get_by_natural_key(self, email):
        return self.get(email=email)
 
 
class AuthorManager(BaseUserManager):
 
    def create_author(self, first_name, last_name, email, bio, password=None):
        
        if email is None:
            raise TypeError('Users must have an email address.')

        author = Author(first_name=first_name, last_name=last_name, 
                          email=self.normalize_email(email), bio=bio)
        
        author.set_password(password)
        author.save()
        return author
 
 
class NormalUserManager(BaseUserManager):
 
    def create_NormalUser(self, first_name, last_name, email, profession, password=None):

        if email is None:
            raise TypeError('Users must have an email address.')
        
        normal_user = NormalUser(first_name=first_name, last_name=last_name, 
                            email=self.normalize_email(email), profession=profession)
        
        normal_user.set_password(password)
        normal_user.save()
        return normal_user