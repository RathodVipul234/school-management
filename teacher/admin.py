from django.contrib import admin
from .forms import TeacherDetailForm
from .models import TeacherDetail,TeacherDepartment,TeacherClass
# Register your models here.

admin.site.register(TeacherDepartment)
admin.site.register(TeacherDetail)
admin.site.register(TeacherClass)
