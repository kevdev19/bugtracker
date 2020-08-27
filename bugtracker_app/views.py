from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from bugtracker_app.models import CustomUserModel, Ticket

from .forms import TicketForm


def index_view(request):
    new_tickets = Ticket.objects.filter(status='New')
    done_tickets = Ticket.objects.filter(status='Done')
    in_progress_tickets = Ticket.objects.filter(status='In Progress')
    invalid_tickets = Ticket.objects.filter(status='Invalid')
    return render(request, 'index.html', {"new_tickets": new_tickets, "done_tickets": done_tickets, "in_progress_tickets": in_progress_tickets, "invalid_tickets": invalid_tickets, })


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
