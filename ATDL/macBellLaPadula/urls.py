from django.urls import path
from . import views
from django.conf.urls import static
import os
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
]
