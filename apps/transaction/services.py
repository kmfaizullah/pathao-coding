# Python imports

# Django imports
from django.db import transaction


# Third party imports
from rest_framework.exceptions import (
    AuthenticationFailed,
    ValidationError,
)

#self import
from apps.transaction.serializers import (
    WalletSerializer,
    TransactionHistorySerializer,
)
from apps.core.helpers import serializer_perform_create


class WalletApiService():

    def create_wallet(self, request_data):
        request_wallet_data = request_data

        wallet_serializer = WalletSerializer(
                data=request_wallet_data,
                context={"user": None},
            )
        wallet, serialized_wallet = serializer_perform_create(serializer=wallet_serializer)
        return wallet, serialized_wallet

class TransactionHistoryApiService():

    def create_transaction_history(self, request_data):
        request_transaction_history_data = request_data

        history_serializer = TransactionHistorySerializer(
                data=request_transaction_history_data,
                context={"user": None},
            )
        history, serialized_history = serializer_perform_create(serializer=history_serializer)
        return history, serialized_history
