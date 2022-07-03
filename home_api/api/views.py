from django.shortcuts import render
from .models import ScheduleEvent, SmartSwitch
from .serializers import ScheduleSerializer, SwitchSerializer
from rest_framework import viewsets, permissions


# Create your views here.
class SwitchViewSet(viewsets.ModelViewSet):
    queryset = SmartSwitch.objects.all()
    serializer_class = SwitchSerializer
    lookup_field = 'slug'

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = ScheduleEvent.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'pk'
