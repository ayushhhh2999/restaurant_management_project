from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer


class OrderCreateAPIView(APIView):
    """API to create a new order with default Pending status"""

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # status defaults to Pending
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrderStatusAPIView(APIView):
    """API to update order status step by step"""

    allowed_transitions = {
        "Pending": "Preparing",
        "Preparing": "Ready",
        "Ready": "Served",
    }

    def patch(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        new_status = request.data.get("status")

        if not new_status:
            return Response(
                {"error": "Status is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        current_status = order.status

        # Restrict invalid jumps
        if self.allowed_transitions.get(current_status) != new_status:
            return Response(
                {"error": f"Invalid transition from {current_status} to {new_status}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order.status = new_status
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
