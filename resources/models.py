from django.db import models
from django.utils.text import slugify

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
        return self.title
