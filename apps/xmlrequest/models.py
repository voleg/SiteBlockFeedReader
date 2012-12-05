__author__ = 'voleg'
from django.db  import  models
from datetime import datetime

class requestsetings(models.Model):
    operatorname = models.CharField(max_length=64)
    INN_numbers = models.DecimalField(decimal_places=64, max_digits=64)
    orgn = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)



class requestlog(models.Model):
    time = models.TimeField(default=datetime.now, max_length=64)
    date = models.DateTimeField(default=datetime.now, max_length=64)