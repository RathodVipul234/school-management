from django import forms
from .models import TeacherDetail, Test
import os
from django.core.exceptions import ValidationError
from django.forms import formset_factory


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
            'placeholder': "Enter teacher id"
        })
        self.fields['teacher_class'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['teacher_img'].widget.attrs.update({
            'class': 'form-control',
        })


class TestFormTxt(forms.Form):
    questions_txt = forms.CharField(max_length=100)

    class Meta:
        model = Test
        excludes = ('teacher', 'questions', 'questions_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['questions_txt'].label = ""

        self.fields['questions_txt'].widget.attrs.update({
            # 'class': 'form-control',
            'placeholder': 'Enter text for your questions',
            'style': "border-radius:5px;border-color:gray;width:325px;height:40px"
        })


class TestForm(forms.Form):
    questions = forms.FileField()

    class Meta:
        model = Test
        excludes = ('teacher', 'questions_txt','questions_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['questions'].label = ""
        self.fields['questions'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'upload your questions in audio or video format'
        })

    def clean(self):
        self.cleaned_data = super().clean()
        questions = self.cleaned_data['questions']
        name, extension = os.path.splitext(questions.name)
        if extension in ['.mp3', '.wav']:
            return self.cleaned_data
        elif extension in ['.mp4', '.mpg', '.mpeg']:
            return self.cleaned_data
        else:
            raise ValidationError("enter valid file ")


test_formset = formset_factory(TestForm, extra=1, max_num=10)
test_formset_txt = formset_factory(TestFormTxt, extra=1, max_num=10)
