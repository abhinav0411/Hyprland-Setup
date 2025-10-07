from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
