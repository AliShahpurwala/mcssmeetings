"""mcssmeetings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from login import views as loginViews
from meeting import views as meetingViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginViews.login_view, name="login_view"),
    path('home/', meetingViews.home_view, name="home_view"),
    path('createMeeting/', meetingViews.create_new_meeting_view, name="create_new_meeting_view"),
    path('meeting/', meetingViews.meeting_view, name="meeting_view"),
    path('create_new_agenda_item/', meetingViews.create_new_agenda_item),
    path('create_new_comment_item/', meetingViews.create_new_comment_item),
    path('logout/', loginViews.logout_view, name="logout_view")
]
