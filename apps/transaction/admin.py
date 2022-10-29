from django.contrib import admin
from apps.transaction.models import (
    Wallet,
    TransactionHistory,
)

admin.site.register(Wallet)
admin.site.register(TransactionHistory)