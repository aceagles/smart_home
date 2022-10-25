from django.contrib import admin
from heating_control.models import ScheduledEvent, Usage

# Register your models here.

admin.site.register(ScheduledEvent)
admin.site.register(Usage)
