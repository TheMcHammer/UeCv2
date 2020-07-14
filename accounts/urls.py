from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
#from .views import (
#    register_counsel,
#    register_student,
#)

urlpatterns = [
    #path('', LoginView.as_view(template_name='login.html')),
    path('', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('group/', views.group_check, name='group'),
    #path('register_counsel/', register_counsel.as_view(), name='register_counsel'),
    #path('register_student/', register_student.as_view(), name='register_student'),
]