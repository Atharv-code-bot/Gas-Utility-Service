from django.db import models
from django.contrib.auth.models import User
import pytz

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    details = models.TextField()
    attached_file = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Type: {self.service_type}, Status: {self.status}, Details: {self.details}, Attached File: {self.attached_file.url if self.attached_file else 'No File'}, Created At: {self.created_at}, Updated At: {self.updated_at}"
