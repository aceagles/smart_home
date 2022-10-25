from .models import ScheduleEvent, SmartSwitch
from rest_framework import serializers


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleEvent
        fields = ("pk", "switch", "time", "action")
        lookup_field = "pk"


class SwitchSerializer(serializers.ModelSerializer):
    events = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = SmartSwitch
        fields = ("pk", "name", "status_url", "toggle_url", "slug", "events")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
