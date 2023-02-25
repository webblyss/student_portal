from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Student

class StudentBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            student = Student.objects.get(email=email)
            user = student.user
            if user.check_password(password):
                return user
        except Student.DoesNotExist:
            return None
