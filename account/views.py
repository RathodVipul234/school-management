from django.shortcuts import render, redirect
from .forms import signupForm, signinForm
from .models import Admin
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from django.core.exceptions import ValidationError


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None


# Create your views here.

def Signup(request):
    form = signupForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password = make_password(form.cleaned_data['password'])
            sign_up.save()
            messages.success(request, "registration successfully")
            return redirect('home')

    else:
        form = signupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def Signin(request):
    form = signinForm(request.POST)
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        username = form.data['email']
        password = form.data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully login..")
            return render(request, 'dashboard.html', {'user': user})
        else:
            if Admin.objects.filter(Q(username=username) | Q(email=username)).exists():
                messages.error(request, "Invalid password")
            else:
                messages.error(request, "user not found")
    else:
        form = signinForm()
    return render(request, 'accounts/login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('home')
