from rest_framework import permissions


class IsEnvelopeOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an Envelope to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
