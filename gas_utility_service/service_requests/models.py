from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    Service_type = [
        ('GAS_LEAK','Gas Leak'),
        ('INSTALLATION','Installation'),
        ('BILLING_ISSUE','Billing Issue'),
        ('OTHER','Other'),
    ]

    Status_Choice = [
        ('PENDING','Pending'),
        ('IN_PROGRESS','In Progress'),
        ('RESOLVED','Resolved'),
        ('CLOSED','Closed'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    service_type = models.CharField(max_length=20, choices=Service_type, default='OTHER')
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status_Choice, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer.username} - {self.get_service_type_display()} ({self.status})"
