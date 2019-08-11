from django.shortcuts import render
from django.template.response import TemplateResponse
from . import forms
from django.http import JsonResponse
from .static.core.passwordUtilities import password
from .models import LoginLogSection, LoginSection, User, UserSalt, UserSaltSection, Section
import random
import datetime
import hashlib
# Create your views here.
def index(request):
    registerForm = forms.RegisterForm()
    userForm = forms.UserForm()
    challForm = forms.ChallengeForm()
    #them muoi
    signup = forms.RegisterForm()
    signin = forms.Login()
    #bruteforce
    userBF = forms.User()
    pwdBF = forms.Password()
    contex = {'form_mk_basic': registerForm, 'form_user' : userForm, 'form_loginChall': challForm, 'form_signup_salt': signup, 'form_signin_salt': signin, 'form_bruteforce_user': userBF, 'form_bruteforce_pwd': pwdBF}
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
            login_section = LoginSection(ID_section = logsection, challen_num = challengeNumber, login_time = datetime.datetime.now(), login_false = 0)
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

def salt_signup(request):
    data = {}
    if request.method == "POST":
        username_post = request.POST.get('username')
        #check username is not exits
        queryResult = UserSalt.objects.filter(us_username= username_post)
        if len(queryResult) == 0:
            pwd_post = request.POST.get('password')
            pwd = password.Password(pwd_post)
            pwd.themmuoi()
            pwd.hashMD5()
            usersalt = UserSalt.objects.create(us_username= username_post, us_password = pwd.md5, us_salt = pwd.salt)
            data ={'statusCode': 200, 'mess': 'Đăng kí thành công'}
        else:
            data = {'statucCode': 401, 'mess': 'Tài khoản đã tồn tại'}
    else:
        data ={'statusCode': 400, 'mess': 'Lỗi đăng kí'}
    return JsonResponse(data)

def salt_signin(request):
    data = {}
    if request.method == "POST":
        username_post = request.POST.get('username')
        # check username is not exits
        queryResult = UserSalt.objects.filter(us_username=username_post)
        if len(queryResult) == 1:
            user = queryResult[0]
            pwd_post = request.POST.get('password')
            pwd = pwd_post + user.us_salt
            mypwd = password.Password(pwd)
            mypwd.hashMD5()
            if mypwd.md5 == user.us_password:
                mypwd.checkPassword()
                anderson = {'Mật khẩu + salt lưu trong CSDL': pwd, 'Độ dài': mypwd.lenght, 'Xác suất Anderson': mypwd.andersonP,
                        'Độ mạnh yếu': mypwd.nhan}
                data = {'statusCode': 200, 'mess': 'Đăng nhập thành công', 'pwdProperties': anderson}
            else:
                data = {'statucCode': 401, 'mess': 'Sai mật khẩu'}
        else:
            data = {'statucCode': 401, 'mess': 'Tài khoản không tồn tại'}
    else:
        data = {'statusCode': 400, 'mess': 'Lỗi đăng kí'}
    return JsonResponse(data)

def prevBrutefoceCheckusername(request):
    data = {}
    if request.method == 'POST':
        username_post = request.POST.get('username')
        queryResult = UserSalt.objects.filter(us_username=username_post)
        if len(queryResult) == 1:
            user = queryResult[0]
            #tao section
            section = UserSaltSection(uss_IDuser = user, uss_status = False, uss_fistTime = datetime.datetime.now(datetime.timezone.utc))
            section.save()
            sectionInfo = Section(s_IDsection = section, s_FalseTimes = 0, s_lastTime = datetime.datetime.now(datetime.timezone.utc))
            sectionInfo.save()
            data = {'statusCode': 200, 'mess': 'Mời nhập mật khẩu', 'sectionID': section.uss_IDsection}
        else:
            data = {'statusCode': 401, 'mess': 'Tài khoản không tồn tại'}
    return JsonResponse(data)

def prevBrutefoce(request):
    data = {}
    if request.method == 'POST':
        pwd_post = request.POST.get('password')
        section_post = request.POST.get('sectionID')
        querry = UserSaltSection.objects.filter(uss_IDsection = section_post)
        if(len(querry) == 1):
            section = UserSaltSection.objects.get(uss_IDsection = section_post)
            user = section.uss_IDuser
            sectionInfo = section.usersaltsection.all()[0]
            #check password
            if section.uss_status == False:
                lastTime = sectionInfo.s_lastTime
                fistTime = section.uss_fistTime
                #tinh thoi gian phat:
                falseTimes = int(sectionInfo.s_FalseTimes)
                waitPentime = falseTimes * 2
                penaltyTime = lastTime + datetime.timedelta(seconds= falseTimes * 2)
                if datetime.datetime.now(datetime.timezone.utc) < penaltyTime:
                    data = {'statusCode': 402, 'mess': 'Bạn phải đợi hết thời gian', 'penaltyTime':penaltyTime.time(), 'mustwait': waitPentime}
                else:
                    mypwd = password.Password(pwd_post + user.us_salt)
                    mypwd.hashMD5()
                    if mypwd.md5 == user.us_password:
                        section.uss_status = True
                        section.save()
                        data = {'statusCode': 200, 'mess': 'Đăng nhập thành công'}
                    else:
                        data = {'statusCode': 401, 'mess': 'Sai mật khẩu'}
                        sectionInfo.s_FalseTimes = int(sectionInfo.s_FalseTimes) + 1
                        sectionInfo.s_lastTime = datetime.datetime.now(datetime.timezone.utc)
                        sectionInfo.save()
            else:
                data = {'statusCode': 401, 'mess': 'section out of date'}
    else:   data = {'statusCode': 500, 'mess': 'co loi'}
    return JsonResponse(data)
