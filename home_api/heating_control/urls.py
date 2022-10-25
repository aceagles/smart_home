from django.urls import path
import heating_control.views as views

urlpatterns = [
    path("", views.toggle_form),
    path("btn", views.toggle_btn, name="toggle_button"),
    path("usage", views.update_usage)
]
