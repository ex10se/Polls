from rest_framework.permissions import AllowAny


class ActionBasedPermission(AllowAny):
    """
    Разрешения на разные запросы для разных категорий пользователей
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False
