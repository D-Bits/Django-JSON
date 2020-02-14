from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Textbook(models.Model):

    title = models.CharField(max_length=200)
    properties = JSONField()

    def __str__(self):
        
        return self.title