"""
URL configuration for meeting_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from website.views import welcome, about
# from meetings.views import detail, rooms_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"), # Associate the url with the 'welcome' view, with url mapping name "welcome"
    path('about', about),
    path('meetings/', include('meetings.urls')),
    # path('meetings/<int:id>', detail, name="detail"), # Expects there to be a route /meetings/{id} with id being an integer, on the 'detail' view, with url name path 'detail'
    # path('rooms', rooms_list, name="rooms"),
    path('auth/', include('django.contrib.auth.urls')) # For authentication
 ]
