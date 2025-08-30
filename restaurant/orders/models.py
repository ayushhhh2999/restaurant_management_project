from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  # points to Role

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.menu_item.name} x {self.quantity}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
