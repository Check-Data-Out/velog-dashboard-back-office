from django.db import models

from common.models import TimeStampedModel
from users.utils import generate_random_group_id


class User(TimeStampedModel):
    """
    대시보드 사용자 모델
    """

    velog_uuid = models.UUIDField(
        blank=False, null=False, unique=True, verbose_name="사용자 UUID"
    )
    access_token = models.TextField(
        blank=False, null=False, verbose_name="Access Token"
    )
    refresh_token = models.TextField(
        blank=False, null=False, verbose_name="Refresh Token"
    )
    group_id = models.IntegerField(
        blank=True,
        null=False,
        default=generate_random_group_id,
        verbose_name="그룹 ID",
    )
    email = models.EmailField(
        blank=False, null=False, unique=True, verbose_name="이메일"
    )
    is_active = models.BooleanField(
        default=True, null=False, verbose_name="활성 여부"
    )

    def __str__(self) -> str:
        return f"{self.velog_uuid}"

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자 목록"
