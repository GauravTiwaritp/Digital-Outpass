from django.db import models

# Create your models here.
class Outpass(models.Model):
    username=models.CharField(max_length=45)
    roll=models.CharField(max_length=15,blank=False)
    Hostel=models.CharField(max_length=25)
    Reason=models.CharField(max_length=1000)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=1000,null=False)
    Phone_no=models.IntegerField(null=False)
    duration=models.IntegerField(null=False)
    status=models.CharField(max_length=50,default="Not yet accepted")