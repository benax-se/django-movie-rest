from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        print(request.user.is_superuser)
        return bool(request.user and request.user.is_superuser)


class IsSenior(BasePermission):

    def has_permission(self, request, view):
        return request.user.profile.position.name == "Senior" if not request.user.is_anonymous else False

