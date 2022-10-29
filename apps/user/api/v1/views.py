# Python imports

# Django imports
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Third party imports


# Self imports
from apps.core.mixins import ModelViewSetPermissionMixin
from apps.user.serializers import UserSerializer
from apps.user.services import (
    UserApiService,
)
from apps.user.models import User


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        login_service = UserApiService(request=request)
        response = login_service.login()
        return Response(data=response, status=HTTP_200_OK)

class UserModelViewSet(ModelViewSetPermissionMixin):
    model = User
    serializer_class = UserSerializer
    lookup_field = "uid"
    http_method_names = ["post",]
    permission_classes_by_action = {
        "create": [AllowAny],
    }

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(**kwargs)

    def create(self, request, *args, **kwargs):
        admin_service = UserApiService(request=request)
        user = admin_service.create_user()
        return Response(
            {"message": "User has been successfully created"}, status=HTTP_200_OK
        )


