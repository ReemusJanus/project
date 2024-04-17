from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    description = models.CharField(max_length=255)
    punch_in_time = models.DateTimeField()
    punch_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')