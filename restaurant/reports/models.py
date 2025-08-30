# Create your models here.
from django.db import models

class SalesReport(models.Model):
    date = models.DateField(auto_now_add=True)
    total_orders = models.IntegerField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    top_item = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} - {self.total_sales}"
