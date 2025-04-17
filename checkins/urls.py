from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_checkin, name='checkin-home'),
]