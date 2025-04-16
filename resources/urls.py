from django.urls import path
from . import views
urlpatterns = [
    path('', views.resource_list, name='resource-list-home'),
    path('<int:pk>/', views.resource_detail, name='resource-detail'),
]