from django.shortcuts import render
from .models import SmartSwitch
from .serializers import SwitchSerializer
from rest_framework import viewsets, permissions


# Create your views here.
class SwitchViewSet(viewsets.ModelViewSet):
    queryset = SmartSwitch.objects.all()
    serializer_class = SwitchSerializer
    lookup_field = 'slug'