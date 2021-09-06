from django.db import models


class Category(models.Model):
    name = models.CharField(
        blank = False, 
        null = False,
        max_length = 50
    )

    class Meta:
        ordering = ['-name']