from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from .views import (
    counsel,
    counsel_appointment_list,
    appointment_delete,
    counsel_appointment_update,
)

urlpatterns = [
    path('', views.counsel_home, name='counsel_home'),
    path('my_appointment/', views.counsel, name='counsel_appointment'),
    path('create_appointment/', views.counsel_appointment_list, name='counsel_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete, name='appointment_delete'),
    path('create_appointment/update/<int:id>/', counsel_appointment_update, name='counsel_appointment_update'),

]

