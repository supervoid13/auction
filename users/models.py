from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=36, blank=True)
    balance = models.DecimalField(max_digits=11, decimal_places=2, default=0.0)