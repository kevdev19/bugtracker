from django.contrib import admin

from .models import Ticket

# Displays multiple columns in admin panel


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']


admin.site.register(Ticket, TicketAdmin)

# Register your models here.
