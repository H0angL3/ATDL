from django.urls import path
from . import views
from django.conf.urls import static
import os
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('checkAnderson', views.checkAnderson, name='checkAnderson'),
    path('requestLogin', views.userRequest, name='requestLogin'),
    path('challengeResponse',views.challengeResponse, name = 'challengeResponse'),
    path('salt_signup', views.salt_signup, name=  'salt_sinup'),
    path('salt_signin', views.salt_signin, name = 'salt_signin'),
]


urlpatterns += static.static(settings.CSS_PASSWORD_URL, document_root = settings.CSS__PASSWORD_ROOT)
urlpatterns += static.static(settings.JS_PASSWORD_URL, document_root = settings.JS_PASSWORD_ROOT)
