from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('studentView',views.studentView,name="studentView"),
    path('wardenView',views.wardenView,name="wardenView"),
    path('securityView',views.securityView,name="securityView"),
    path('delete/<roll>',views.delete,name='delete'),
    path('delete1/<roll>',views.delete1,name='delete1'),
    path('logout_user',views.logout_user,name="logout_user"),
]  