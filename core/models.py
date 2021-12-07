from django.db import models


class TimeStampedModel(models.Model):
    """
    created, modified file 공통 추상클래스 모델
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


