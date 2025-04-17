"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from checkins import views as checkin_views
from users import views as user_views
from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', core_views.root_page, name='root'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('home/', user_views.home, name='home'),
    path('checkin/', include('checkins.urls')),
    path('profile/', user_views.profile, name="profile"),
    path('communityPost/', include('communityPost.urls')),
    path('resources/', include('resources.urls')),
    path('crisis-support/', core_views.crisis_support, name='crisis-support'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
