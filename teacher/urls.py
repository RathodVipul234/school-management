from django.urls import path
from .views import teacherRegisteration,teacherList,teacherUpdate,deleteTeacher


urlpatterns = [
    path('register/', teacherRegisteration, name='teacher_registration'),
    path('teacher_list/', teacherList, name='teacher_list'),
    path('teacher_update/<int:id>/', teacherUpdate, name='teacher_update'),
    path('delete_teacher/<int:id>/', deleteTeacher, name='delete_teacher'),
]


