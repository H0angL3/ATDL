from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
import hashlib
from django.core.files.base import File, ContentFile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *
import os
import json

STORAGE_ROOT = settings.BELL_ROOT

def index(request):
    loginForm = forms.Login()
    context = {'login': loginForm}
    return TemplateResponse(request, 'baseBellLaPadula/base.html',context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        query = User.objects.filter(username = username, password = password)
        if len(query) == 1:
            response = {'status': 200, 'message': ("thanh cong"), 'url': 'loggedin'}
            return JsonResponse(response)
        else:
            return HttpResponse('sai tai khoan')
    else:
        return index(request)
def loggedin(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user = User.objects.get(username = username)
        userPriv = user.get_secret_classifications()
        userInfo = {'username': username, 'secretLV': {cate:classi for cate, classi in userPriv.items()}    }
        #XAC DINH QUYEN CUA USER TREN CAC DOI TUONG
        read_list = {}
        fileid = 0
        for obj in (user.all_objects_can_read()):
            #user infomation
            path = os.path.relpath(obj.path, STORAGE_ROOT)
            baseurl = '/macBellLaPadula' + settings.BELL_URL
            url = os.path.join(baseurl, path)
            fileid += 1
            read_list[obj.title] = {'id' : fileid,'fileurl': url, 'category': obj.category, 'classification': obj.classification}
            #dua ra ddanh sach cac tep duoc truy cap
        context = {'userinfo': json.dumps(userInfo), 'read_list' : json.dumps(read_list)}
        return render(request, 'baseBellLaPadula/loggedin.html',context= context)
    else:
        return HttpResponse("Ban chua dang nhap")

def newDocument(request):
    if request.session.has_key('username'):
        #danh sach category co the sua
        user = User.objects.get(username = request.session['username'])
        write_types = user.types_write()
        doctypes = []
        list_type = list(write_types.keys())
        count = 0
        for cate in write_types.keys():
            classifis_list = write_types[cate]
            classifis = []
            for i in range(len(classifis_list)):
                count += 1
                classifis.append((count , classifis_list[i]))
            doctypes.append((cate, classifis))
        newdocForm = forms.NewDocument(doctypes)
        request.session['categrories'] = doctypes
        return TemplateResponse(request, 'baseBellLaPadula/newDocument.html', {'newdoc': newdocForm})

def createDoc(request):
    docClassification = ()
    data = {}
    if request.session.has_key('username'):
        if request.method == "POST":
            doctypes = request.session['categrories']
            category = request.POST.get('categories')
            for cate in doctypes:
                for classi in cate[1]:
                    if str(category) == str(classi[0]):
                        docClassification = (cate[0], classi[1])
            #save content to file
            content = request.POST.get('content')
            fileTitle = request.POST.get('title')
            fileName = str(hashlib.md5(content.encode('utf-8')).hexdigest()) + '.txt'
            filePath = STORAGE_ROOT + '/' + docClassification[0]+ '/' + fileName
            #luu object vao csdl
            newObj = Object(title = fileTitle, filename = fileName, path = filePath, category = docClassification[0], classification = docClassification[1])
            newObj.save()
            default_storage.save(filePath, ContentFile(content))
            return HttpResponse(200)
    return HttpResponse(400)


