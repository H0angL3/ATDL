from django.contrib import admin
from .models import User
from .models import LoginLogSection, LoginSection, UserSalt
# Register your models here.
class UserAdminDB(admin.ModelAdmin):
    list_display = ['ID_user', 'user_name', 'password']
admin.site.register(User, UserAdminDB)

class LoginSectionAdminDB(admin.ModelAdmin):
    list_display = ['ID_section', 'login_time', 'login_false', 'challen_num']
admin.site.register(LoginSection, LoginSectionAdminDB)

class LoginLogSecstionAdmin(admin.ModelAdmin):
    list_display = ['ID_section', 'ID_user', 'status']
admin.site.register(LoginLogSection, LoginLogSecstionAdmin)

class UserSaltAdmin(admin.ModelAdmin):
    list_display = ['us_IDuser', 'us_username', 'us_password', 'us_salt']
admin.site.register(UserSalt, UserSaltAdmin)