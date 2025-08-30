from celery import shared_task
from django.utils.timezone import now
from .models import SalesReport
from orders.models import Order, OrderItem

from reports import models  # Assuming you have these models

@shared_task
def generate_sales_report():
    today = now().date()

    # Aggregate orders of the day
    orders = Order.objects.filter(created_at__date=today)
    total_orders = orders.count()
    total_sales = sum(order.total_price for order in orders)

    # Find top-selling item
    top_item = (
        OrderItem.objects.filter(order__in=orders)
        .values("item__name")
        .annotate(total_qty=models.Sum("quantity"))
        .order_by("-total_qty")
        .first()
    )

    SalesReport.objects.create(
        date=today,
        total_orders=total_orders,
        total_sales=total_sales,
        top_item=top_item["item__name"] if top_item else "N/A",
    )

    return {
        "date": str(today),
        "total_orders": total_orders,
        "total_sales": total_sales,
        "top_item": top_item["item__name"] if top_item else "N/A",
    }
