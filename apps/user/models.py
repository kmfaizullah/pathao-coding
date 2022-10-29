import uuid
from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, user_name, password=None):
        """
        Creates and saves a User with the given user name and password.
        """
        if not user_name:
            raise ValueError('Users must have an user name address')

        user = self.model(
            user_name=self.normalize_email(user_name),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            user_name,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    uid = models.UUIDField(
        verbose_name="UUID",
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )

    user_name = models.CharField(
        verbose_name="User Name",
        db_column="user_name",
        max_length=255,
        unique=True,
    )

    password = models.CharField(
        verbose_name="Password",
        db_column="password",
        max_length=150,
    )

    is_active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    is_superuser = models.BooleanField(
        verbose_name="Is Superuser",
        default=False,
    )

    is_staff = models.BooleanField(
        verbose_name="Is Staff",
        default=False,
    )

    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        editable=False,
    )


    objects = UserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["password"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    def __str__(self):
        return f"{self.user_name}"