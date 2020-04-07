from django.db import models
from django.contrib.postgres.fields import ArrayField

class Sorting(models.Model):

    algorithm = models.TextField()
    numbers = ArrayField(ArrayField(models.IntegerField()))