from django.db import models

# Create your models here.

class Currency(models.Model):
    currency = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    