from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


def is_token_expired(token):
    return token.created < timezone.now() - timedelta(
        seconds=getattr(settings, 'TOKEN_EXPIRED_AFTER_SECONDS', 24*60*60))


class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.select_related('user').get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed(_('Invalid Token'))

        try:
            user = token.user
        except (get_user_model().DoesNotExist, AttributeError):
            raise AuthenticationFailed(_('Invalid User'))

        if not user.is_active:
            raise AuthenticationFailed(_('User is not active'))

        if is_token_expired(token):
            raise AuthenticationFailed(_('The Token is expired'))

        return user, token
