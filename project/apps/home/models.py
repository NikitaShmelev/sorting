from django.db import models
from django.contrib.postgres.fields import ArrayField

class Sorting(models.Model):
    Bubble = 'Bubble'
    Insertion = 'Insertion'
    Merge = 'Merge'
    algorithm = models.CharField(
        max_length=9,
        choices=[
            (Bubble,'Bubble',), 
            (Insertion, 'Insertion',),
            (Merge, 'Merge'),
            ],
        default='Buble',
    )
    numbers = ArrayField(ArrayField(models.IntegerField()))