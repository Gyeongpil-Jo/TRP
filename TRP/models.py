from django.db import models
from django.contrib.auth.models import User


class Inform(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()