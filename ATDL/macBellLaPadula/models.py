from django.db import models

#user table
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 100)
    password = models.CharField(max_length=100)

class Sc_User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.CharField(max_length=100)
    classification = models.CharField(max_length= 100)

class Object(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100)
    path = models.FileField(max_length=200)
    category = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
