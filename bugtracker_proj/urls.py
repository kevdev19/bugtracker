"""bugtracker_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from bugtracker_app.views import index_view, add_ticket, ticket_detail_view, user_ticket_list_view, login_view

urlpatterns = [
    path('', index_view, name='homepage'),
    path('add_ticket/', add_ticket, name='addticket'),
    path('ticket/<int:ticket_id>/', ticket_detail_view, name='ticketdetail'),
    path('user/<str:user_name>/', user_ticket_list_view, name='userticketlist'),
    path('login/', login_view, name="loginpage"),
    path('admin/', admin.site.urls),
]
