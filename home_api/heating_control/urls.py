from django.urls import path
import heating_control.views as views
from .api import ControllerView


urlpatterns = [
    path("", views.toggle_form),
    path("btn", views.toggle_btn, name="toggle_button"),
    path("check", ControllerView.as_view())
]
