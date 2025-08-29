from rest_framework import serializers
from .models import Menu, Order


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "price", "available"]


class OrderSerializer(serializers.ModelSerializer):
    waiter = serializers.ReadOnlyField(source="waiter.username")  # Auto assign waiter

    class Meta:
        model = Order
        fields = ["id", "waiter", "menu_item", "quantity", "created_at", "is_paid"]
        read_only_fields = ["created_at", "is_paid"]

    def create(self, validated_data):
        """Automatically set the waiter from logged-in user"""
        request = self.context.get("request")
        validated_data["waiter"] = request.user
        return super().create(validated_data)
