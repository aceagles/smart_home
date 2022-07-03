from django.db import models
from django.utils.text import slugify

# Create your models here.
class SmartSwitch(models.Model):
    status_url = models.URLField()
    toggle_url = models.URLField()
    slug = models.SlugField()
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SmartSwitch, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class ScheduleEvent(models.Model):
    class Actions(models.TextChoices):
        ON = "ON", "On"
        OFF = "OFF", "Off"
        TOG = "TOG", "Toggle"
    time = models.TimeField()
    action = models.CharField(choices=Actions.choices, max_length=6)
    switch = models.ForeignKey(SmartSwitch, on_delete=models.CASCADE, related_name="events")
