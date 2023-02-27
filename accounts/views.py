from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def register(request):
    
    
    return render(request,'register.html')




def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user) 
            if user.is_student:
                return redirect(request,"home")
            elif user.is_instructor:
                return print('you are a instructor')
        else:
            context = {"error": "Invalid email or password"}
            messages.info(request,context)
            return render(request, "login.html", context)
    else:
        return render(request, "login.html")



