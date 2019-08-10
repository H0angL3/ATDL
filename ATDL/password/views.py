from django.shortcuts import render
from django.template.response import TemplateResponse
from . import forms
from django.http import JsonResponse
from .static.core.passwordUtilities import password
from .models import LoginLogSection, LoginSection, User
import random
from datetime import datetime
import hashlib
# Create your views here.
def index(request):
    registerForm = forms.RegisterForm()
    userForm = forms.UserForm()
    challForm = forms.ChallengeForm()
    contex = {'form_mk_basic': registerForm, 'form_user' : userForm, 'form_loginChall': challForm}
    return TemplateResponse(request, 'base.html', contex)

def checkAnderson(request):
    data = {}
    if request.method == "POST":
        # tinh toan anderson
        pwd = request.POST.get('password')
        mypass = password.Password(pwd)
        mypass.checkPassword()
        data = {'Mật khẩu': pwd, 'Độ dài': mypass.lenght, 'Xác suất Anderson': mypass.andersonP, 'Độ mạnh yếu': mypass.nhan}
        return JsonResponse(data)
    else:
        return JsonResponse({'err':'false'})

def userRequest(request):
    data = {}
    if request.method == "GET":
        userName = request.GET.get('chal_username')
        queryResult = User.objects.filter(user_name = userName)
        if len(queryResult) == 1:
            userID = getattr(queryResult[0], 'ID_user')
            print(queryResult.values())
            #tao so r ngau nhien luu vao csdl login va gui cho user
            challengeNumber = random.randint(1000,9999)
            #luu section vao loginlogsection
            logsection = LoginLogSection(ID_user = User.objects.get(ID_user = userID), status = False)
            logsection.save()
            #luu section vao loginsesstion
            login_section = LoginSection(ID_section = logsection, challen_num = challengeNumber, login_time = datetime.now(), login_false = 0)
            login_section.save()
            print('section', getattr(logsection,'ID_section'))
            data = {'statusCode': 200, 'user': userName, 'challenge_number': challengeNumber, 'sectionID': getattr(logsection,'ID_section')}
        else:
            data = {'statusCode': 401,'error': 'user name does not exist'}
    else:
        data ={'statusCode': 405, 'error': 'unknow error'}
    return JsonResponse(data)

def challengeResponse(request):
    if request.method == 'POST':
        sectionID = request.POST.get('sectionID')
        hashpassword = request.POST.get('hashpassword')
        logsection = LoginLogSection.objects.filter(ID_section = sectionID)
        if len(logsection) == 1:
            logsection = logsection[0]
            user = logsection.ID_user
            section = logsection.loginsection.all()[0]
            print(user.password + section.challen_num)
            passwordReal = hashlib.md5((user.password + section.challen_num).encode('utf-8')).hexdigest()
            if str(passwordReal) == hashpassword:
                logsection.status = True
                logsection.save()
                return JsonResponse({"statusCode": 200, 'mess': 'Đăng nhập thàn công'})
            else:
                return JsonResponse({'statusCode': 401, 'mess': 'Sai mật khẩu hoặc mã xác nhận'})
        else:
            return JsonResponse({"error":'something wrongs'})

    return JsonResponse({})