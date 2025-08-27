from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready"),
        ("Served", "Served"),
    ]

    customer_name = models.CharField(max_length=100)
    items = models.TextField()  # Can be JSON string or comma-separated list
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    def __str__(self):
        return f"Order {self.id} - {self.customer_name} ({self.status})"
