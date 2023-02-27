from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def courses(request):
    
    
    return render(request,'courses.html')



def addCourses(request,pk):
    
    
    return HttpResponse({'message':"updated"})




