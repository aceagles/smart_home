from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from .models import MockSwitch

# Create your views here.
def get_status(request, slug=None):
    if slug:
        try:
            mock_switch = MockSwitch.objects.get(slug=slug)
        except MockSwitch.DoesNotExist:
            return HttpResponseNotFound()
        return JsonResponse({"status": mock_switch.status}, safe=False)
    return HttpResponseNotFound()


def toggle_status(request, slug=None):
    if slug:
        try:
            mock_switch = MockSwitch.objects.get(slug=slug)
        except MockSwitch.DoesNotExist:
            return HttpResponseNotFound()
        mock_switch.status = not mock_switch.status
        mock_switch.save()
        return JsonResponse({"status": mock_switch.status}, safe=False)
    return HttpResponseNotFound()
