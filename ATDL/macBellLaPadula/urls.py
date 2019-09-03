from django.urls import path
from . import views
from django.conf.urls import static
import os
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name = 'login'),
    path('loggedin', views.loggedin, name = 'loggedin'),
    path('new-document', views.newDocument, name = 'new document'),
    path('create-document', views.createDoc, name = 'create document')
]
urlpatterns += static.static(settings.BELL_URL, document_root=settings.BELL_ROOT)
urlpatterns += static.static('/css/', document_root=os.path.join(settings.BASE_DIR, 'macBellLaPadula/static/css'))
urlpatterns += static.static('/js/', document_root=os.path.join(settings.BASE_DIR, 'macBellLaPadula/static/js'))
