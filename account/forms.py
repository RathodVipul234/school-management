from django import forms
from .models import Admin
from django.core.exceptions import ValidationError


class signupForm(forms.ModelForm):
    retype_password = forms.CharField(label="retype", widget=forms.TextInput)

    class Meta:
        model = Admin
        fields = ("name", 'admin_id', 'email', 'username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "name"
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "username"
        })
        self.fields['admin_id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "admin_id"
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "email"
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "password"
        })

        self.fields['retype_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "retype_password"
        })

    def clean(self):
        self.cleaned_data = super(signupForm, self).clean()

        email = self.cleaned_data['email']
        admin_id = self.cleaned_data['admin_id']
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['retype_password']
        if Admin.objects.filter(email=email).exists():
            raise ValidationError("Email already registered")
        elif Admin.objects.filter(admin_id=admin_id).exists():
            raise ValidationError("admin id already registered")
        if pass1 != pass2:
            raise ValidationError("password and confirm password not matched")


class signinForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Admin
        fields = ('email', 'password',)
        labels = {
            'email': 'username'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.input_type = "text"
        self.fields['email'].widget.lable = "text"
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email or username'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "password"
        })

    # def clean(self):
    #     self.cleaned_data = super(signinForm, self).clean()
    #
    #     email = self.cleaned_data['email']
    #     password = self.cleaned_data['password']
    #
    #     return self.cleaned_data
