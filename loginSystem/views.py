from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from loginSystem.models import Student,Warden,Officer
from django.contrib import messages
# Create your views here.
def student(request):
    messages.error(request, 'Details not correct.')
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            
            return redirect("Maincommunication/studentView")

        else:
          #  print("no")
            # No backend authenticated the credentials
            return redirect('student')
    return render(request,"student.html")

def warden(request):
    messages.error(request, 'Details not correct.')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("Maincommunication/wardenView")

        else:
          #  print("no")
            # No backend authenticated the credentials
            return redirect('warden')
        
    
    return render(request,"warden.html")    

def security(request):
    messages.error(request, 'Details not correct.')
    if request.method=='POST':
        print("hello")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("Maincommunication/securityView")
        else:
            messages.error(request, 'Details not correct.')
            return redirect('security')    
    return render(request,"security.html")  

def section(request):
    return render(request,"section.html")      