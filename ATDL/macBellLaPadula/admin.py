from django.contrib import admin
from .models import User, Sc_User, Object

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password']
admin.site.register(User, UserAdmin)


class Sc_UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'category', 'classification']
admin.site.register(Sc_User, Sc_UserAdmin)


class ObjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'filename','path', 'category', 'classification']
admin.site.register(Object, ObjectAdmin)
