from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Outpass
from django.template import loader
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib import messages
from loginSystem.models import Student,Warden,Officer
# Create your views here.
#Hostel_Name
def studentView (request):
    print(10)
    messages.success(request, 'Outpass request submitted.')
    messages.error(request, 'Details not correct.')
    if request.method=="POST":
        username=request.POST.get("username")
        rollNo=request.POST.get("roll")
        hostel=request.POST.get("Hostel")   
        phone=request.POST.get("phone_no")
        reason=request.POST.get("Reason")
        date=request.POST.get("date")
        time=request.POST.get("time")
        duration=request.POST.get("duration")
        a=(User.objects.filter(username=request.user.username).all().values_list("username",flat=True))
        q=list(a)
        correct=False
        for i in q:
            if(i==request.user.username):
                print(i)
                print("jeete")
                correct=True
        a1=((Student.objects.filter(Name=username)).all().values_list())
     #   detail=Outpass.objects.filter(roll=rollNo).all().values('username','roll','date','time','status') 
        q1=list(a1)
        print((q1[0][1]))
        a1=(q1[0][1]==username)  
        a2=(q1[0][0]==rollNo)
        a3=(q1[0][2]==hostel)
        print(a1==True)
        print(q1[0][2])
        print(a2)         
        if (a1==True) and (correct==True) and (a2==True) and (a3==True):
              print("hello")
              messages.success(request, 'Outpass request submitted.')
              detail=Outpass.objects.filter(roll=rollNo).all().values('username','roll','date','time','status','Reason')
              if(detail):
                 return render(request,"studentpage.html",context={"content":detail})
              else:
                 ins=Outpass(username=username,roll=rollNo,Hostel=hostel,Phone_no=phone,Reason=reason,date=date,time=time,duration=duration)
                 ins.save() 
                 print("correct")
                 return render(request,'studentpage.html',context={"content":detail})
              
        else:
            
            print("incorrect")
    try:
        print("hello")
        detail=Outpass.objects.filter(roll=request.user.username).all().values('username','roll','date','time','status','Reason','Hostel')
        print(detail)
        if (detail): 
            return render(request,"studentpage.html",context={"content":detail})
    except:     
        return render(request,'studentpage.html')
    return render(request,'studentpage.html')
def wardenView (request):
    q=Warden.objects.filter(user_Name=request.user.username).all().values_list( 'Hostel_Assigned',flat=True)
    qlist=list(q)
    a=[]
    details=[]
    for i in qlist:
        a=Outpass.objects.filter(Hostel=i).exclude(status="accepted").all().values('username','roll','date','time','status','Reason','Hostel')
    for i in a:
        print(a[0])
        if(a.model('status')=="rejected"):
            print(1)
 
  #  print(qlist)
  #  print((a))
    if request.method=='POST':
       print("hello")
       action=request.POST.get("enquiry")
       print(action)
       words=action.split('_')
       print(words)
       if(words[0]=="accepted"):
        q5=Outpass.objects.get(roll=words[1])
        print(q5.roll)
        q5.status="accepted"
        q5.save()
        for i in qlist:
           a=Outpass.objects.filter(Hostel=i).exclude(status="accepted").all().values('username','roll','date','time','status','Reason','Hostel')
   #     print(q5.status)
   #     print(1)
       if(words[0]=="rejected"):
        q5=Outpass.objects.get(roll=words[1])
        print(q5.roll)
        q5.status="rejected"
        q5.save()
        for i in qlist:
            a=Outpass.objects.filter(Hostel=i).exclude(status="accepted").all().values('username','roll','date','time','status','Reason','Hostel')
    #    print(q5.status)
    #    print(1) 
    return render(request,"wardenpage.html",context={"content":a})

def securityView(request):
    a5=Outpass.objects.filter(status="accepted").all().values()
    print("galti")
    print("security view succesfully accepted")
    return render(request,"securitypage.html",context={"content":a5})

def delete(request,roll):
    print("helolo")
    event=Outpass.objects.get(roll=roll)
    print(event)
    event.delete()
    return redirect ('securityView')

def delete1(request,roll):
    print("helolo")
    event=Outpass.objects.get(roll=roll)
    print(event)
    event.delete()
    return redirect ('studentView')

def logout_user(request):
    logout(request)
    return redirect("section")