from django.db import models
from django.utils.text import slugify

# Create your models here.
class SmartSwitch(models.Model):
    status_url = models.URLField()
    toggle_url = models.URLField()
    slug = models.SlugField()
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        super(SmartSwitch, self).save(*args, **kwargs)