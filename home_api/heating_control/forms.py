from ast import Mod
from django import forms
from django.forms import ModelForm
from heating_control.models import ScheduledEvent
from datetime import datetime


class ScheduleForm(ModelForm):
    class Meta:
        model = ScheduledEvent
        fields = ["command", "start_time", "repeat"]

    start_time = forms.CharField(
        widget=forms.TextInput(attrs={"type": "datetime-local"}), initial=datetime.now
    )
