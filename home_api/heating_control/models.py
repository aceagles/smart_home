from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class Usage(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    is_on = models.BooleanField()
    def __str__(self):
        return f"{self.date} - {'On' if self.is_on else 'Off' }"


class ScheduledEvent(models.Model):

    start_time = models.DateTimeField(auto_now_add=False, default=timezone.now)
    completed = models.BooleanField(default=False)

    ON = "ON"
    OFF = "OFF"
    TOG = "TOG"
    TOGGLE_CHOICES = ((ON, "On"), (OFF, "Off"), (TOG, "Toggle"))
    command = models.CharField(max_length=6, choices=TOGGLE_CHOICES, default=TOG)

    def __str__(self):
        return f"{self.command} - {self.start_time}"