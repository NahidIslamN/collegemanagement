from django.contrib import admin
from baseapp.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class userModels(UserAdmin):
    list_display = ["username","user_type"]


admin.site.register(CustomUser,userModels)
admin.site.register(Teacher)
admin.site.register(Head_Of_Dep)
admin.site.register(Subjects)
admin.site.register(Group)
admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(Shift)
admin.site.register(Departments)
admin.site.register(subject_group_for_student)
admin.site.register(Student)
admin.site.register(AttendanceObject)
admin.site.register(Apply_for_leave)
admin.site.register(Student_mark)
admin.site.register(message_model_for_user)
