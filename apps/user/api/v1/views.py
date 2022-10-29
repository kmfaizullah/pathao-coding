# Python imports

# Django imports
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

# Third party imports


# Self imports
from apps.core.mixins import ModelViewSetPermissionMixin
from apps.user.serializers import UserSerializer
from apps.user.services import (
    UserApiService,
)
from apps.user.models import User

from apps.core.permissions import (
    IsUser,
)


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
    http_method_names = ["post","patch", "get"]
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

    @action(
        detail=True,
        methods=["patch"],
        url_path="amount_transfer",
        url_name="amount_transfer",
        permission_classes=[IsUser],
    )
    def user_wallet_to_wallet_amount_transfer(self, request, *args, **kwargs):
        user_obj = self.get_object()
        user_service = UserApiService(request=request)
        history = user_service.amount_transfer_from_one_wallet_to_another_wallet(
            from_user=user_obj
        )
        return Response(
            {"message": "User requested amount has been successfully transferred"}, status=HTTP_200_OK
        )

    @action(
        detail=True,
        methods=["get"],
        url_path="transaction_history",
        url_name="transaction_history",
        permission_classes=[IsUser],
    )
    def particular_user_transaction_history(self, request, *args, **kwargs):
        user_obj = self.get_object()
        user_service = UserApiService(request=request)
        txn_history = user_service.user_transaction_history(
            request_user=user_obj
        )
        return Response(
            {"data": txn_history}, status=HTTP_200_OK
        )

    @action(
        detail=False,
        methods=["get"],
        url_path="all_user_balance",
        url_name="all_user_balance",
        permission_classes=[AllowAny],
    )
    def user_total_balance(self, request, *args, **kwargs):
        user_service = UserApiService(request=request)
        all_total_balance = user_service.user_total_balance()
        return Response(
            {"total_balance": all_total_balance}, status=HTTP_200_OK
        )

    @action(
        detail=True,
        methods=["get"],
        url_path="get_balance",
        url_name="get_balance",
        permission_classes=[IsUser],
    )
    def particular_user_balance(self, request, *args, **kwargs):
        user_obj = self.get_object()
        balance = user_obj.user_having_wallet.amount
        return Response(
            {"amount": balance}, status=HTTP_200_OK
        )


