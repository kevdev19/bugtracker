from django.shortcuts import render

from bugtracker_app.models import CustomUserModel, Ticket


def index_view(request):
    new_tickets = Ticket.objects.filter(status='New')
    done_tickets = Ticket.objects.filter(status='Done')
    in_progress_tickets = Ticket.objects.filter(status='In Progress')
    invalid_tickets = Ticket.objects.filter(status='Invalid')
    return render(request, 'index.html', {"new_tickets": new_tickets, "done_tickets": done_tickets, "in_progress_tickets": in_progress_tickets, "invalid_tickets": invalid_tickets, })
