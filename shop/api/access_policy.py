from shop.base_access_policy import BaseAccessPolicy


class CategoryProductAccessPolicy(BaseAccessPolicy):
    statements = [
        {"action": ["list", "retrieve"], "principal": ["*"], "effect": "allow"},
        {
            "action": ["create", "update", "partial_update", "destroy", "get_summary"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "is_administrator",
        },
    ]
