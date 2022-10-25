from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/status", views.get_status),
    path("<slug:slug>/toggle", views.toggle_status),
]
