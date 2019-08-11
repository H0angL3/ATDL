from django.db import models



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


# Create your models here.
class UserSalt(models.Model):
    us_IDuser = models.AutoField(primary_key= True)
    us_username = models.CharField(max_length=100)
    us_password = models.CharField(max_length=100)
    us_salt = models.CharField(max_length=50)

class UserSaltSection(models.Model):
    uss_IDsection = models.AutoField(primary_key= True)
    uss_IDuser = models.ForeignKey(UserSalt, on_delete=models.CASCADE)
    uss_fistTime = models.DateTimeField()
    uss_status = models.BooleanField(default= False)

class Section(models.Model):
    s_IDsection = models.ForeignKey(UserSaltSection, on_delete= models.CASCADE, related_name = 'usersaltsection')
    s_FalseTimes = models.CharField(max_length=10, default= 0)
    s_lastTime = models.DateTimeField()