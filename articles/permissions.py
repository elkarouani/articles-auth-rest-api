from rest_framework.permissions import BasePermission


class IsProvider(BasePermission):
    message = "Providers only can create new articles"

    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_provider

class IsOwner(BasePermission):
    message = "Only article owner can delete his own article"

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return request.user == obj.user