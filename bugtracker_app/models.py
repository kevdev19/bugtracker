from django.db import models
from django.utils.timezone import now

from customuser_app.models import CustomUserModel


class Ticket(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = 'New',
        IN_PROGRESS = 'In Progress',
        DONE = 'Done',
        INVALID = 'Invalid',
    title = models.CharField(max_length=90)
    time_submitted = models.DateTimeField(
        default=now, editable=False)
    description = models.TextField(max_length=255)
    createdby = models.ForeignKey(
        CustomUserModel, null=True, on_delete=models.CASCADE, related_name='createdby')
    status = models.CharField(
        max_length=32,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW
    )
    assignedto = models.CharField(
        max_length=255, default='None')
    completedby = models.CharField(max_length=255, default='None')

    # Displays multiple columns in admin panel
    def __str__(self):
        ret = self.title + ',' + self.status
        return ret
    # Also displays multiple columns in admin panel

    class Meta:
        unique_together = ['title']
