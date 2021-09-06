from django.db import models
from api_category.models import Category

class Offer(models.Model):
    
    title = models.CharField(
        blank = False, 
        null = False,
        max_length = 50
    )
    description = models.TextField(
        blank = False, 
        null = False
    )
    price = models.DecimalField(
        blank = False, 
        null = False,
        max_digits = 10,
        decimal_places = 2
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    
    # many to one
    category = models.ForeignKey(
        Category, 
        on_delete = models.CASCADE,
        blank = False,
        null = False
    )
