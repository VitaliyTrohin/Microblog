from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Пользователи могут редактировать только свои записи.
    Админы могут редактировать все записи.
    Для всех остальных запросы только на чтение (GET).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Админы могут выполнять любые действия.
    Для всех остальных запросы только на чтение (GET).
    """
    def has_permission(self, request, view):
        return request.user.is_staff or request.method in permissions.SAFE_METHODS


class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Суперпользователи могут выполнять любые действия.
    Для всех остальных запросы только на чтение (GET).
    """
    def has_permission(self, request, view):
        return request.user.is_superuser or request.method in permissions.SAFE_METHODS