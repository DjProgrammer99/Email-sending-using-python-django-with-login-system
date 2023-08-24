from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.login_page),
    path('sendmail',v.add_mail),
    path('success',v.success),
    path('logout',v.logout_view),
    path('adduser',v.adduser),
    
]
