from django.db import models

# Create your models here.
# models.py

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Define other fields
