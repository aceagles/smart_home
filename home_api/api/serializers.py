from .models import SmartSwitch
from rest_framework import serializers

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartSwitch
        fields = ('url', 'name', 'status_url', 'toggle_url')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }