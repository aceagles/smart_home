from django.contrib import admin
from api.models import SmartSwitch, ScheduleEvent

# Register your models here.
class SwitchAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ("name", "slug")


admin.site.register(SmartSwitch, SwitchAdmin)
admin.site.register(ScheduleEvent)
