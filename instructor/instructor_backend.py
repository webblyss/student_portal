from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Instructor

class InstructorBackend(BaseBackend):

    def authenticate(self, request, staff_id=None, password=None, **kwargs):
        try:
            instructor = Instructor.objects.get(staff_id=staff_id)
            user = instructor.user
            if user.check_password(password):
                return user
        except Instructor.DoesNotExist:
            return None
