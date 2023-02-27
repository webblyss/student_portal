from django.contrib import admin
from .models import GeneralMessage,Notification,Message,StudentCourseRegistration

# Register your models here.

admin.site.register(GeneralMessage) 
admin.site.register(Notification) 
admin.site.register(Message) 
admin.site.register(StudentCourseRegistration) 