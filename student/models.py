from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentManager(BaseUserManager):
    def create_user(self, email, firstName, lastName, phone, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstName, lastName, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstName", "lastName", "phone"]

    objects = StudentManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
