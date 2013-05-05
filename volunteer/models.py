from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Charity(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField(max_length=256, default=None)
    description = models.TextField(max_length=1028)

class Service(models.Model):
    name = models.CharField(max_length=256)
    available = models.BooleanField(default=True)
    provider = models.ForeignKey(User)
    charity = models.ForeignKey(Charity)
    ammount = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    description = models.TextField(max_length=1028)

    def __unicode__(self):
        return self.name

class Donation(models.Model):
    service = models.ForeignKey(Service)
    provider = models.ForeignKey(User, null=True, related_name='provider')
    receiver = models.ForeignKey(User, null=True, related_name='receiver')

    def __unicode__(self):
        return self.service.name

