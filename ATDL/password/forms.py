from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    confirmPassword = forms.CharField(label= "Confirm password", max_length= 100)

class Login(forms.Form):
    username =  forms.CharField(label="Username", max_length= 100)
    password = forms.CharField(label="Password", max_length= 100)
class UserForm(forms.Form):
    chal_username = forms.CharField(label='Username', max_length= 100)

class ChallengeForm(forms.Form):
    chal_password = forms.CharField(label='Password', max_length=100, required=False)
    serverChalNum = forms.CharField(label='Mã xác nhận', max_length=100, required=False)

class User(forms.Form):
    username = forms.CharField(max_length =100, label='username')

class Password(forms.Form):
    password = forms.CharField(max_length= 100, label='password')
