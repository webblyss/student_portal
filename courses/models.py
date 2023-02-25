from django.db import models
from django.contrib.auth.models import User
from student.models import Student
from instructor.models import Instructor
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    
    
    def __str__(self):
        return self.name
    


class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("student", "course"),)

    def __str__(self):
        return f"{self.student} - {self.course}"







