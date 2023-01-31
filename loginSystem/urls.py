from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('student',views.student,name="student"),
    path('warden',views.warden,name="warden"),
    path('security',views.security,name="security"),
    path('',views.section,name="section"),
]