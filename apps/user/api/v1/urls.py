from django.urls import path
from rest_framework import routers

from apps.user.api.v1.views import (
    UserLoginApiView,
)

router = routers.SimpleRouter()
# router.register('v1/users', UserLoginApiView, 'user')

urlpatterns = [

    path('v1/user/login/', UserLoginApiView.as_view(), name='user_login'),

] + router.urls