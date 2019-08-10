from django.db import models

# Create your models here.
class UserSalt(models.Model):
    us_IDuser = models.AutoField(primary_key= True)
    us_username = models.CharField(max_length=100)
    us_password = models.CharField(max_length=100)
    us_salt = models.CharField(max_length=50)

class User(models.Model):
    ID_user = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class LoginLogSection(models.Model):
    ID_section = models.AutoField(primary_key=True)
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False) #trang thai login thanh cong hay that bai

class LoginSection(models.Model):
    ID_section = models.ForeignKey(LoginLogSection, on_delete=models.CASCADE, related_name='loginsection')
    challen_num = models.CharField(max_length=10) #so thach thuc
    login_time = models.DateTimeField() #thoi gian phien
    login_false = models.CharField(max_length=10) #so lan sai lien tuc\\


