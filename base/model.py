from django.db import models

from base.constant import Status
from base.manager import BaseManger


class BaseModel(models.Model):
    status = models.PositiveIntegerField(choices=Status.choices, default=Status.NORMAL)

    objects = BaseManger()

    class Meta:
        abstract = True
