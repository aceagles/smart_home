from django.http import HttpResponse
from django.shortcuts import render
from .models import ScheduleEvent, SmartSwitch
from .serializers import ScheduleSerializer, SwitchSerializer
from rest_framework import viewsets, permissions
from rest_framework.renderers import JSONRenderer


# Create your views here.
class SwitchViewSet(viewsets.ModelViewSet):
    queryset = SmartSwitch.objects.all()
    serializer_class = SwitchSerializer
    lookup_field = 'slug'

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = ScheduleEvent.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        sched = self.get_object()
        sched.delete()

        return HttpResponse(
            JSONRenderer().render( 
                SwitchSerializer(SmartSwitch.objects.all(), many=True).data), 
                content_type="application/json"
                )