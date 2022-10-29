# Python imports

# Django imports
from rest_framework import serializers

# Third party imports

# Self imports
from apps.core.serializers import DynamicFieldsModelSerializer
from apps.transaction.models import (
    Wallet,
    TransactionHistory,
)


class WalletSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"

class TransactionHistorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = "__all__"