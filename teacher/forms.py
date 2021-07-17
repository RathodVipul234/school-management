from django import forms
from .models import TeacherDetail


class TeacherDetailForm(forms.ModelForm):
    class Meta:
        model = TeacherDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter teacher name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter teacher email'
        })

        self.fields['age'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter teacher age'
        })

        self.fields['birth_date'].widget.input_type = 'date'
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['gender'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['joining_date'].widget.input_type = 'date'
        self.fields['joining_date'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['salary'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter teacher salary'
        })
        self.fields['teacher_department'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['teacher_id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder':"Enter teacher id"
        })
        self.fields['teacher_class'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['teacher_img'].widget.attrs.update({
            'class': 'form-control',
        })

