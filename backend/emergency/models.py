from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class EmergencyReport(models.Model):
    EMERGENCY_TYPES = [
        ('fire', 'Fire'),
        ('flood', 'Flood'),
        ('crime', 'Crime'),
        ('medical', 'Medical'),
        ('earthquake', 'Earthquake'),
        ('others', 'Others'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    emergency_type = models.CharField(max_length=20, choices=EMERGENCY_TYPES)
    description = models.TextField()
    location_text = models.CharField(max_length=255)  # Street or area description
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    photo = models.ImageField(upload_to='emergency_photos/', blank=True, null=True)
    contact_number = models.CharField(max_length=20)
    is_anonymous = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_emergency_type_display()} @ {self.location_text} ({self.status})"


class EmergencyFeedback(models.Model):
    emergency = models.OneToOneField(EmergencyReport, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ])
    comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for Emergency #{self.emergency.id}"
