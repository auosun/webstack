from django.db import models


class Status(models.IntegerChoices):
    DELETED = 0
    NORMAL = 1
