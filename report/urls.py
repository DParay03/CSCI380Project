
from django.urls import path
from .views import report_views

urlpatterns = [
    path('', report_views, name='report'),
]