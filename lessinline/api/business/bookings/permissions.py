from rest_framework.permissions import BasePermission


class IsBookingServiceOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.service.business.owner == request.user
