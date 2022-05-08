import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class feedback(models.Model):
    mail = models.CharField(max_length=200)
    created_at = models.DateTimeField('created_at')
    def __str__(self):
        return self.mail