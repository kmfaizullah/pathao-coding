# Python imports
from locale import currency
import uuid

# Django imports
from django.db import models

# Third party imports


# Self imports
from apps.core.models import BaseModel


class Wallet(BaseModel):

    user = models.OneToOneField(
        to="user.User",
        verbose_name="User Wallet",
        db_column="user_wallet",
        related_name="user_having_wallet",
        on_delete=models.CASCADE,
    )
    amount = models.FloatField(
        verbose_name="User wallet amount",
        db_column="wallet_amount",
        blank=True,
        null=True,
        default=5000.00,
    )
    currency_type = models.CharField(
        verbose_name="Currency Type",
        db_column="currency_type",
        default='BDT',
        max_length=125,
    )

    def __str__(self):
        return f"{self.user.user_name}-{self.amount}"

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"
        db_table = "wallet"


class TransactionHistory(BaseModel):

    class TransactionTypes(models.TextChoices):
        DEBIT = "Debit", "debit"
        CREDIT = "Credit", "credit"
        DEAFAULT_AMOUNT = "Default_amount", "default_amount"

    from_user = models.ForeignKey(
        to="user.User",
        verbose_name="From User",
        db_column="from_user",
        related_name="user_who_sends",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    to_user = models.ForeignKey(
        to="user.User",
        verbose_name="To User",
        db_column="to_user",
        related_name="user_who_receives",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    transaction_amount = models.FloatField(
        verbose_name="Transaction Amount",
        db_column="transaction_amount",
        default=0.00,
    )

    transaction_id = models.UUIDField(
        verbose_name="UUID",
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )

    transaction_type = models.CharField(
        verbose_name="Transaction Type",
        db_column="transaction_type",
        max_length=25,
        choices=TransactionTypes.choices,
    )

    def __str__(self):
        if self.from_user and self.to_user:
            return f"{self.from_user.user_name} sends {self.transaction_amount} to {self.to_user.user_name}"
        else:
            return f"Default transaction amount {self.transaction_amount} sends to {self.to_user.user_name}"

    class Meta:
        verbose_name = "TransactionHistory"
        verbose_name_plural = "TransactionHistries"
        db_table = "transaction_history"