from django.urls import path
from rest_framework import routers

from apps.user.api.v1.views import (
    UserLoginApiView,
    UserModelViewSet,
)

router = routers.SimpleRouter()
router.register('v1/user', UserModelViewSet, 'user')

urlpatterns = [

    path('v1/user/login/', UserLoginApiView.as_view(), name='user_login'),

] + router.urls