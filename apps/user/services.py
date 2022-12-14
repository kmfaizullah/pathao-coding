# Python imports
from datetime import datetime

# Django imports
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.db import transaction
from apps.transaction.models import Wallet, TransactionHistory
from apps.user.models import User


# Third party imports
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import (
    AuthenticationFailed,
    ValidationError,
)

#self import
from apps.user.serializers import (
    LoginSerializer,
    UserSerializer,
)
from apps.core.helpers import serializer_perform_create
from apps.transaction.services import (
    WalletApiService,
    TransactionHistoryApiService,
)




user_model = get_user_model()


class UserApiService():
    def __init__(self, request: object) -> None:
        self.request = request

    def get_user_token(self, user: object) -> dict:
        """
        This is for retreiving user information with token.

        Args:
            user (object): request user object

        Returns:
            dict: user token
        """
        token = Token.objects.filter(user=user).first()
        if token:
            Token.objects.filter(user=user).delete()

        token = Token.objects.create(user=user)
        return token

    def login(self) -> dict:
        """
        This is for user login.

        Raises:
            NotFound: raise error if requested user is not found

        Returns:
            dict: information after successfully logged in
        """
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user_name = serializer.data.get('user_name', None)
        password = serializer.data.get('password', None)
        user = authenticate(user_name=user_name, password=password)
        if not user:
            raise AuthenticationFailed (detail=f"{user_name} is not a valid user")

        user_token = self.get_user_token(user)

        user_data={
            'user_name': user.user_name,
            'token': user_token.key,
            'user_uid': user.uid,
        }
        return user_data

    @transaction.atomic
    def create_user(self) ->None:
        """
        This code block contains code for user creation

        Raises:
            ValidationError: rasie validation error if any criteria fails
        """
        request_user_data = self.request.data
        user_name = request_user_data.get('user_name', None)
        pin = request_user_data.get('pin',None)
        if not user_name or not pin:
            raise ValidationError ({"error":"Valid user name and PIN is required"})
        if pin and len(pin)>5:
            raise ValidationError ({"error":"Pin should be at max 5"})

        user_req_data={
            'user_name': user_name,
            'password': pin
        }
        user_serializer = UserSerializer(
                data=user_req_data,
                context={"user": self.request.user},
            )
        user, serialized_user = serializer_perform_create(serializer=user_serializer)
        user.set_password(pin)
        user.save()

        wallet_obj = WalletApiService()
        wallet = wallet_obj.create_wallet(
            request_data={'user': user.pk}
        )

        txn_history_data={
            'to_user': user.pk,
            'transaction_amount': 5000.00,
            'transaction_type': 'Default_amount'
        }
        txn_history_obj = TransactionHistoryApiService()
        txn_data = txn_history_obj.create_transaction_history(
            request_data=txn_history_data
        )

    @transaction.atomic
    def amount_transfer_from_one_wallet_to_another_wallet(self, from_user) ->None:
        """
        This code block is responsible for user walter transfer

        Args:
            from_user (object): user who requests for transaction

        Raises:
           validation error if any criteria falis
        """
        request_transaction_data = self.request.data
        transaction_amount = request_transaction_data.get('amount', None)
        to_user = request_transaction_data.get('to_user', None)
        transaction_type = request_transaction_data.get('transaction_type', None)

        if not transaction_amount or not to_user or not transaction_type:
            raise ValidationError ({"error":"to user, amount and transaction type is required"})

        to_user_obj = user_model.objects.filter(user_name=to_user).first()
        if not to_user_obj:
            raise ValidationError ({"error":"Please enter a valid to user name"})

        if to_user_obj.pk == from_user.pk:
            raise ValidationError ({"error":"Same wallet transfer is prohibited"})

        user_wallet = from_user.user_having_wallet.amount
        if transaction_amount > user_wallet:
            raise ValidationError ({"error": "You do not have enough amount to transfer"})


        to_user_wallet = Wallet.objects.filter(user = to_user_obj).first()
        from_user_wallet = Wallet.objects.filter(user=from_user).first()
        to_user_wallet.amount = to_user_wallet.amount + transaction_amount
        from_user_wallet.amount = from_user_wallet.amount - transaction_amount
        to_user_wallet.save()
        from_user_wallet.save()
        txn_history_data={
            'from_user': from_user.pk,
            'to_user': to_user_obj.pk,
            'transaction_amount': transaction_amount,
            'transaction_type': transaction_type
        }
        txn_history_obj = TransactionHistoryApiService()
        txn_data = txn_history_obj.create_transaction_history(
            request_data=txn_history_data
        )

    def format_transaction_data(self, data) ->object:
        """
        This is to process user transaction data

        Args:
            data (object): user transaction data object

        Returns:
            object: user formated data
        """
        return {
                'from_user': data.from_user.user_name if data.from_user else None,
                'to_user': data.to_user.user_name,
                'transaction_type': data.transaction_id,
                'transaction_date': data.created_at,
                'amount': data.transaction_amount,
            }
    def user_transaction_history(self,request_user)->object:
        """
        This code block is for getting a specific user transaction history

        Args:
            request_user (obj): user who requests for transaction

        Returns:
            object: User transaction history object
        """
        user_data_history =[]
        all_debit_amount = TransactionHistory.objects.filter(
            from_user = request_user
        )
        all_credit_amount = TransactionHistory.objects.filter(
            to_user = request_user
        )
        for debit_history in all_debit_amount:
            user_data_history.append(self.format_transaction_data(data=debit_history))
        for credit_history in all_credit_amount:
            user_data_history.append(self.format_transaction_data(data=credit_history))

        user_data_history.sort(key=lambda item:item['transaction_date'], reverse=True)

        return user_data_history

    def user_total_balance(self):
        """
        This code block is responsible calculating user total balance

        Returns:
            float: user total balance amount
        """
        user_total_balance = 0.00
        all_wallet_data = Wallet.objects.all()
        for wallet in all_wallet_data:
            user_total_balance = user_total_balance + wallet.amount
        return user_total_balance


