from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BrazilData(models.Model):
    date = models.DateField('date')
    cases = models.PositiveIntegerField('cases', default=0)
    deaths = models.PositiveIntegerField('deaths', default=0)

    def __str__(self):
        return "{}-{}-{}".format(self.date, self.cases, self.deaths)

class SudesteData(models.Model):
    date = models.DateField('date')
    cases = models.PositiveIntegerField('cases', default=0)
    deaths = models.PositiveIntegerField('deaths', default=0)

    def __str__(self):
        return "{}-{}-{}".format(self.date, self.cases, self.deaths)

class SaoPauloData(models.Model):
    date = models.DateField('date')
    cases = models.PositiveIntegerField('cases', default=0)
    deaths = models.PositiveIntegerField('deaths', default=0)

    def __str__(self):
        return "{}-{}-{}".format(self.date, self.cases, self.deaths)
