from django.db import models

from base.constant import Status


class BaseManger(models.Manager):

    def get_queryset(self):
        return super(BaseManger, self).get_queryset().filter(status=Status.NORMAL)
