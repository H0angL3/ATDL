from django.contrib import admin
from .models import User
from .models import LoginLogSection, LoginSection, UserSalt, UserSaltSection,Section
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

class UserSaltSectionAmin(admin.ModelAdmin):
    list_display = ['uss_IDsection', 'uss_IDuser', 'uss_fistTime', 'uss_status']
admin.site.register(UserSaltSection, UserSaltSectionAmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ['s_IDsection', 's_FalseTimes', 's_lastTime']
admin.site.register(Section, SectionAdmin)
