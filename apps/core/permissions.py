from rest_framework.permissions import BasePermission


class IsUser(BasePermission):

    def has_permission(self, request, view):
        print("++++++ here is the requested user +++", request.user)
        if not request.user.is_authenticated:
            return False
        return True

