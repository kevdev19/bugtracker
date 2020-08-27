from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from bugtracker_app.models import CustomUserModel, Ticket

from .forms import TicketForm

import datetime


def index_view(request):
    # These variables make multiple calls to the database
    # You could instead do:
    # all_tickets = Ticket.objects.all()
    # Then use if statement nested in your for loop
    new_tickets = Ticket.objects.filter(status='New')
    done_tickets = Ticket.objects.filter(status='Done')
    in_progress_tickets = Ticket.objects.filter(status='In Progress')
    invalid_tickets = Ticket.objects.filter(status='Invalid')
    # The following two lines calculate difference between time ticket submitted and now
    # resource link: https://tinyurl.com/yyjtydtk
    dt_submitted = Ticket.objects.dates('time_submitted', kind='day')
    now = timezone.now()
    return render(request, 'index.html', {"new_tickets": new_tickets, "done_tickets": done_tickets, "in_progress_tickets": in_progress_tickets, "invalid_tickets": invalid_tickets, "dt_submitted": dt_submitted, "now": now})


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


def ticket_detail_view(request, ticket_id):
    ticket_detail_objs = Ticket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail.html', {"ticket_detail_objs": ticket_detail_objs})
