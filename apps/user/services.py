# Python imports
from datetime import datetime

# Django imports
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.db import transaction


# Third party imports
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import (
    AuthenticationFailed,
)

#self import
from apps.user.serializers import (
    LoginSerializer,
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

    def create_user(self):
        request_user_data = self.request.data
        # user_name = 
        pass