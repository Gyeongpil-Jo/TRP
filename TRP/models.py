from django.db import models
from django.contrib.auth.models import User


class Inform(models.Model):
    # only User can generate Inform
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    files = models.FileField(upload_to="files", blank=True)
    start_date = models.DateTimeField()