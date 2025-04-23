from django.db import models

# Create your models here.
class CrisisSupport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True)
    category = models.CharField(max_length=50, choices=[
        ('Emergency', 'Emergency'),
        ('Substance Abuse', 'Substance Abuse'),
        ('Youth Support', 'Youth Support'),
        ('LGBTQ+', 'LGBTQ+'),
        ('Other', 'Other'),
    ])
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
