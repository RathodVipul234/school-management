from django.db import models

# Create your models here.

class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=100)
    class_short_form = models.CharField(max_length=10)

    def __str__(self):
        return  self.class_name

class StudentSectionInfo(models.Model):
    section_name = models.CharField(max_length=20)

    def __str__(self):
        return self.section_name


class StudentDetail(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male","Male"),
        ("female","Female")
    )
    gender = models.CharField(choices=gender_choice,max_length=10)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    student_id = models.CharField(max_length=50, unique=True)
    class_type = models.ForeignKey(StudentClassInfo,on_delete=models.CASCADE)
    section_type = models.ForeignKey(StudentSectionInfo,on_delete=models.CASCADE)
    student_number = models.CharField(max_length=12)
    student_img = models.ImageField(upload_to="media/student_img")

    def __str__(self):
        return self.name


