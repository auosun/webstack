from django.db import models

from base.model import BaseModel


class Menu(BaseModel):
    class Meta:
        db_table = 'menu'
        verbose_name = '分组'
        verbose_name_plural = verbose_name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='分组名')
    icon = models.CharField(max_length=255, default='linecons-star', verbose_name='分组图标')
    weight = models.IntegerField(default=1, verbose_name='分组权重')

    def __str__(self):
        return self.name


class Website(BaseModel):
    class Meta:
        db_table = 'website'
        verbose_name = '网站'
        verbose_name_plural = verbose_name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='网站名称')
    description = models.CharField(max_length=255, verbose_name='网站描述')
    url = models.URLField(verbose_name='网站链接')
    title = models.CharField(max_length=255, verbose_name='原始标题')
    icon = models.URLField(verbose_name='网站图标',
                           default='https://aupicgo.oss-cn-shanghai.aliyuncs.com/img/20200910125957.ico')
    weight = models.IntegerField(verbose_name='网站权重', default=1)
    menu = models.ForeignKey(Menu, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name
