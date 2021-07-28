from django.urls import path
from .views import *

urlpatterns = [
    path('register/', teacherRegisteration, name='teacher_registration'),
    path('teacher_list/', teacherList, name='teacher_list'),
    path('teacher_update/<int:id>/', teacherUpdate, name='teacher_update'),
    path('delete_teacher/<int:id>/', deleteTeacher, name='delete_teacher'),
    path('test/', create_test, name='test'),
    path('test-questions/', test_questions, name='test_questions'),
    path('update-questions/<int:id>/', update_questions, name='update_questions'),

]
