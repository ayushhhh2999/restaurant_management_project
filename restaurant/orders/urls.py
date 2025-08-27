from django.urls import path
from .views import OrderCreateAPIView, UpdateOrderStatusAPIView

urlpatterns = [
    path("orders/", OrderCreateAPIView.as_view(), name="create_order"),
    path("orders/<int:pk>/status/", UpdateOrderStatusAPIView.as_view(), name="update_order_status"),
]
