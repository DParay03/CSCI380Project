from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class JournalEntry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self): # define the canonical URL for a model instance - tells Django how to get the URL to view the detail page for specific Journal Object
        return reverse('journal-detail', kwargs={'pk': self.pk})