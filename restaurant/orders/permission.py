from rest_framework.permissions import BasePermission

class IsManagerOrAdmin(BasePermission):
    """Allow only Managers or Admins to modify menu"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["Manager", "Admin"]


class IsWaiter(BasePermission):
    """Allow only Waiters to create orders"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "Waiter"


class IsCashier(BasePermission):
    """Allow only Cashiers to process payments"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "Cashier"
