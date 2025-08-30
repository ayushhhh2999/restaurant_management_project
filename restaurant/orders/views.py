from rest_framework import generics
from .models import Menu, Order
from .serializers import MenuSerializer, OrderSerializer
from .permission import IsManagerOrAdmin, IsWaiter, IsCashier


class MenuCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsManagerOrAdmin]  # only Managers/Admins can create


class OrderCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsWaiter]  # only Waiters can create orders


class ProcessPaymentAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsCashier]  # only Cashiers can update payments
