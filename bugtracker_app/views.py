from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone

from bugtracker_app.models import CustomUserModel, Ticket

from .forms import TicketForm, LoginForm

import datetime


# @login_required
def index_view(request):
    # These variables make multiple calls to the database
    # You could instead do:
    # all_tickets = Ticket.objects.all()
    # Then use if statement nested in your for loop
    new_tickets = Ticket.objects.filter(status='New')
    done_tickets = Ticket.objects.filter(status='Done')
    in_progress_tickets = Ticket.objects.filter(status='In Progress')
    invalid_tickets = Ticket.objects.filter(status='Invalid')
    # The following two line calculate difference between time ticket submitted and now
    # resource link: https://tinyurl.com/yyjtydtk
    now = timezone.now()
    return render(request, 'index.html', {"new_tickets": new_tickets, "done_tickets": done_tickets, "in_progress_tickets": in_progress_tickets, "invalid_tickets": invalid_tickets, "now": now})


@login_required
def add_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Ticket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                createdby=request.user
            )
            if new_ticket:
                return HttpResponseRedirect(reverse("homepage"))

    form = TicketForm()
    return render(request, "add_ticket.html", {"ticket_form": form})


# Displays each ticket in detail
def ticket_detail_view(request, ticket_id):
    ticket_detail_objs = Ticket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail.html', {"ticket_detail_objs": ticket_detail_objs})


def user_ticket_list_view(request, user_name):
    ticket_list = Ticket.objects.filter(createdby__username=user_name)
    new_tickets = Ticket.objects.filter(status='New')
    now = timezone.now()
    print(ticket_list)
    return render(request, 'user_ticket_list.html', {"ticket_list": ticket_list, "new_tickets": new_tickets, "now": now})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginpage'))
