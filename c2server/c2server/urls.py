"""
URL configuration for c2server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from c2app.views import list_sessions, execute_command
from c2app.views import list_empire_agents, execute_empire_command

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sessions/', list_sessions, name="list_sessions"),
    path('execute/', execute_command, name="execute_command"),
    path('empire/agents/', list_empire_agents, name="list_empire_agents"),
    path('empire/execute/', execute_empire_command, name="execute_empire_command"),
]
