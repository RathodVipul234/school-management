from django import forms
from .models import StudentDetail
from django.core.exceptions import ValidationError


class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "student name"
        })       

        self.fields['age'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "age"
        })

        self.fields['gender'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "gender"
        })

        self.fields['father_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "father_name"
        })

        self.fields['mother_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "mother_name"
        })

        self.fields['academic_year'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "academic_year"
        })

        self.fields['admission_date'].widget.input_type = 'date'
        self.fields['admission_date'].widget.attrs.update({
            'class': 'form-control',

        })

        self.fields['student_id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "student_id"
        })

        self.fields['class_type'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "class_type"
        })

        self.fields['section_type'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "section_type"
        })

        self.fields['student_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "student_number"
        })

        self.fields['student_img'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "student_img"
        })
    def clean(self):
        cleaned_data = super().clean()
        
        student_id = self.cleaned_data['student_id']
        student_number = self.cleaned_data['student_number']
        student_age = self.cleaned_data['age']
        
        if student_age > 30 :
            raise ValidationError("student age not more than 30 year.")

        # elif StudentDetail.objects.filter(student_id=student_id).exists():
        #     raise ValidationError("student id already exists")

        elif len(student_number) != 10:
            raise ValidationError("please enter valid mobile number")




    # widgets = {
    #     'name': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "student name"
    #     }),
    #
    #     'age': forms.NumberInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "Age"
    #     }),
    #
    #     'father_name': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "father name"
    #     }),
    #
    #     'mother_name': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "mother name"
    #     }),
    #
    #     'academic_year': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "Academic year"
    #     }),
    #
    #     'admission_date': forms.DateInput(attrs={
    #         'class': 'form-control',
    #         'type': 'date'
    #     }),
    #
    #     'student_id': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "student Id"
    #     }),
    #
    #     'class_type': forms.Select(attrs={
    #         'class': 'form-control',
    #     }),
    #
    #     'section_type': forms.Select(attrs={
    #         'class': 'form-control',
    #     }),
    #
    #     'student_number': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "student number"
    #     }),
    #     'student_img': forms.FileInput(attrs={
    #         'class': 'form-control',
    #     })
    #
    # }

