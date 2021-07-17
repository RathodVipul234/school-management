from django.db import models


# Create your models here.

class TeacherDepartment(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name


class TeacherClass(models.Model):
    class_name = models.CharField(max_length=100)
    class_short_form = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class TeacherDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    gender_choice = (
        ('Male', "male"),
        ("Female", "female")
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    age = models.IntegerField()
    joining_date = models.DateField()
    salary = models.IntegerField()
    teacher_id = models.CharField(max_length=50, unique=True)
    teacher_department = models.ForeignKey(TeacherDepartment, on_delete=models.CASCADE)
    teacher_class = models.ManyToManyField(TeacherClass)
    teacher_img = models.ImageField(upload_to='media/teacher_img')

    def __str__(self):
        return self.name
