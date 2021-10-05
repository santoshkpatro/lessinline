from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsBusinessOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.business.owner == request.user
