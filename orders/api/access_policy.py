from shop.base_access_policy import BaseAccessPolicy


class OrderAccessPolicy(BaseAccessPolicy):
    statements = [
        {"action": ["create", "list"], "principal": ["authenticated"], "effect": "allow"},
        {
            "action": ["update", "partial_update", "destroy"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "is_owner",
        },
        {
            "action": ["retrieve", "get_order_cost"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "is_admin_or_owner"
        }
    ]

    def is_owner(self, request, view, action) -> bool:
        """
        Check if the user is the owner of the order
        """
        order = view.get_object()
        return request.user == order.customer

    def is_admin_or_owner(self, request, view, action):
        """
        Check if the user is either the owner or the admin
        """
        order = view.get_object()
        return request.user == order.customer or request.user.is_staff
