from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True)
    is_completed=models.BooleanField(default=True)
    create_ad=models.DateTimeField(auto_now_add=True)