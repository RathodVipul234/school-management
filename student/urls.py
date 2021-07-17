from django.urls import path
from .views import studentRegistrations,studentList,studentUpdate,deleteStudent


urlpatterns = [

    path('register/',studentRegistrations,name='student_registration'),
    path('studentlist/',studentList,name='student_list'),
    path('student_update/<int:id>/',studentUpdate,name='student_update'),
    path('delete_student/<int:id>/',deleteStudent,name='delete_student')

]

