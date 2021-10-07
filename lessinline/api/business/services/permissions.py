from rest_framework.permissions import BasePermission


class IsServiceOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.business.owner == request.user
