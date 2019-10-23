from django.db import models

# Create your models here.
from django.forms import forms
from django import forms
from django.urls import reverse


class Job(models.Model):
    job = models.CharField(max_length=50)
    Description = models.TextField()
    HourlyRate = models.CharField(max_length=50)
    MaxHoursPerDay = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('Administer:adminjoblist')

    def __str__(self):
        return self.job



class Machine(models.Model):
    machinecode = models.CharField(max_length=50)
    Descriptions = models.TextField()
    HourlyRate = models.CharField(max_length=50)
    MaxHoursPerDay = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('Administer:adminmachinelist')

    def __str__(self):
        return self.machinecode

class Timecard(models.Model):
    Sitecode = models.CharField(max_length=50)
    nameofcontracter = models.TextField()
    Totalhrs = models.CharField(max_length=50)
    Totalamount = models.CharField(max_length=50)
    State = models.CharField(max_length=50,default='Review')


    def get_absolute_url(self):
        return reverse('Administer:admintimecardlist')



from django.db import models

# Create your models here.

