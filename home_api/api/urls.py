from rest_framework import routers
from api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"switches", views.SwitchViewSet)
router.register(r"event", views.ScheduleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
