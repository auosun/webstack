from django.db import models

from base.constant import Status


class BaseQuerySet(models.QuerySet):
    """
    base queryset for override delete
    """

    def delete(self):
        """ soft delete """
        return super(BaseQuerySet, self).update(status=Status.DELETED)

    def hard_delete(self):
        return super(BaseQuerySet, self).delete()


class BaseManger(models.Manager):
    """
    base manger for filter status
    """

    def get_queryset(self):
        """
        override queryset
        :return: queryset filter status with normal
        """
        return super(BaseManger, self).get_queryset().filter(status=Status.NORMAL)


class BaseModel(models.Model):
    status = models.PositiveIntegerField(choices=Status.choices, default=Status.NORMAL)

    objects = BaseManger.from_queryset(BaseQuerySet)()

    class Meta:
        abstract = True
