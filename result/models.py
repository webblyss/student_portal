from django.db import models
from student.models import Student
from courses.models import Course

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = (("student", "course"),)

    def __str__(self):
        return f"{self.student} - {self.course}: {self.score}"
