from django.contrib import admin

from .models import Student,Warden,Officer
# Register your models here.

admin.site.register(Student)
admin.site.register(Warden)
admin.site.register(Officer)
