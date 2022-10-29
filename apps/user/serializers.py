# Python imports

# Django imports
from rest_framework import serializers

# Third party imports

# Self imports
from apps.user.models import User
from apps.core.serializers import DynamicFieldsModelSerializer

class LoginSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = "__all__"