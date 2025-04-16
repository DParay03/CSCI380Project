from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')  # Only one check-in per user per day

    def __str__(self):
        return f"{self.user.username} - {self.score} on {self.date}"