from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(AbstractUser):
    ROLES = [
        ("Manager", "Manager"),
        ("Admin", "Admin"),
        ("Waiter", "Waiter"),
        ("Cashier", "Cashier"),
    ]

    role = models.CharField(max_length=20, choices=ROLES, default="Waiter")

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.username} - {self.role}"
