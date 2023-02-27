from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth.hashers import make_password

class StudentBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            student = Student.objects.get(email=email)
            user = student.user
            if user.check_password(password):
                return user
        except Student.DoesNotExist:
            return None
        
         # Use make_password to encrypt the password
        if student and student.password == make_password(password):
            return student
