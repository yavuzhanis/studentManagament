from django.contrib import admin
from .models import * 
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel (UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser,UserAdmin)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Staff_leave)