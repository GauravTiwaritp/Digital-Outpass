from django.db import models

# Create your models here.

class Student(models.Model):
    user_Name=models.CharField(max_length=15,primary_key=True)
    
    Name=models.CharField(max_length=15,blank=False)
    Hostel_Name=models.CharField(max_length=25)
    Phone_no=models.IntegerField(null=False)
    Roll_No=models.CharField(max_length=15,null=False)
class Warden(models.Model):
    user_Name=models.CharField(max_length=15,primary_key=True)
    password=models.CharField(max_length=15,blank=False)
    Name=models.CharField(max_length=15,blank=False)
    Hostel_Assigned=models.CharField(max_length=25)
    warden_id=models.CharField(max_length=20)
class Officer(models.Model):
    user_Name=models.CharField(max_length=15,primary_key=True)
    password=models.CharField(max_length=15,blank=False)
    Name=models.CharField(max_length=15,blank=False)    

def __str__(self):
    return self.name
