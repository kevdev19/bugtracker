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

from bugtracker_app import views

urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('add_ticket/', views.add_ticket, name='addticket'),
    path('ticket/<int:ticket_id>/edit/', views.edit_ticket_view, name='edit'),
    path('claim/<int:ticket_id>/', views.claim_ticket_view, name='claim'),
    path('invalid/<int:ticket_id>/', views.invalid_ticket_view, name='invalid'),
    path('complete/<int:ticket_id>/', views.complete_ticket_view, name='complete'),
    path('ticket/<int:ticket_id>/', views.ticket_detail_view, name='ticketdetail'),
    path('user/<str:user_name>/', views.user_ticket_list_view, name='userticketlist'),
    path('login/', views.login_view, name="loginpage"),
    path('logout/', views.logout_view, name="logoutpage"),
    path('admin/', admin.site.urls),
]
