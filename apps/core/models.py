import uuid

from django.db import models
from django.contrib.auth import get_user_model

class BaseModel(models.Model):
    user_model = get_user_model()

    uid = models.UUIDField(
        verbose_name="UUID",
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )

    created_by = models.ForeignKey(
        to=user_model,
        verbose_name="Created by",
        null=True,
        blank=True,
        related_name="%(class)s_created",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True,
        editable=False,
    )

    updated_by = models.ForeignKey(
        to=user_model,
        verbose_name="Updated by",
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        on_delete=models.CASCADE,
    )

    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        auto_now=True,
    )
    class Meta:
        abstract = True