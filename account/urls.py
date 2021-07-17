from django.urls import path
from .views import Signup,Signin,Logout


urlpatterns = [
    path('signup/', Signup, name='signup'),
    path('login/', Signin, name='signin'),
    path('logout/', Logout, name='logout'),
]

