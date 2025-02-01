from django.db import models
import os
# Create your models here.
def student_directory_name(instance, filename):
    return os.path.join('student/media',instance.fullname, filename)

class Student(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)
    course = models.CharField(max_length=50)
    number = models.CharField(max_length=11)
    photo = models.ImageField(upload_to= student_directory_name, default=None, null=True)

    def __str__(self):
        return super().__str__() + self.fullname