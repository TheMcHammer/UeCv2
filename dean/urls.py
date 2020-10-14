from django.urls import path
from . import views
from django.views.generic import TemplateView
from dean.views import DeansView


urlpatterns = [
    path('', DeansView.as_view(), name='dean_home'),
    ]