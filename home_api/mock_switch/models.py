from django.db import models
from django.utils.text import slugify

# Create your models here.


class MockSwitch(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MockSwitch, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
