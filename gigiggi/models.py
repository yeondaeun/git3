from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Booth(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    content = models.TextField()

