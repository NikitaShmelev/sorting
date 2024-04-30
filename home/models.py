from django.db import models
from django.contrib.postgres.fields import ArrayField


class Sorting(models.Model):
    Bubble = "Bubble"
    Insertion = "Insertion"
    Merge = "Merge"
    Shell = "Shell"
    Selection = "Selection"
    algorithm = models.CharField(
        max_length=9,
        choices=[
            (
                Bubble,
                "Bubble",
            ),
            (
                Insertion,
                "Insertion",
            ),
            (Merge, "Merge"),
            (Shell, "Shell"),
        ],
        default="Buble",
    )
    numbers = models.TextField()
    file = models.FileField()
    # Explicitly define a primary key field
    id = models.AutoField(primary_key=True)
