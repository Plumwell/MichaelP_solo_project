from django.db import models
import re

class UserAdmin(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 3:
             errors['fname'] = "The First Name field must contain at least 3 characters!"
        if len(postData['lname']) < 3:
             errors['lname'] = "The Last Name field must contain at least 3 characters!"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = ("Invalid email address!")
        if len(postData['zip']) < 5:
            errors['zip'] = "You must put in a valid zipcode!"
        if len(postData['pw']) < 8:
            errors['pw'] = "The Password field must contain at least 8 characters!"
        if postData['confpw'] != postData['pw']:
            errors['confpw'] = "Your passwords do not match!"
        return errors

class MerchAdmin(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['store']) < 5:
            errors['store'] = "The Store must be more than 5 characters"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = ("Invalid email address!")
        if len(postData['zip']) < 5:
            errors['zip'] = "You must put in a valid zipcode!"
        if len(postData['pw']) < 8:
            errors['pw'] = "The password must be at least 8 characters"
        if postData['confpw'] != postData['pw']:
            errors['confpw'] = "Your passwords do not match!"
        return errors


class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    pw = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserAdmin()

class Merchant(models.Model):
    store = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)
    pw = models.CharField(max_length=30)
    patrons = models.ForeignKey(User, related_name='patrons', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = MerchAdmin()

class Game(models.Model):
    title = models.CharField(max_length=20)
    player = models.CharField(max_length=2)
    gametype = models.CharField(max_length=40)
    desc  = models.CharField(max_length=250)
    fav = models.ManyToManyField(User, related_name='games')


