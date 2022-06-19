from django.db import models

from base.model import BaseModel


class SiteGroup(BaseModel):
    class Meta:
        db_table = 'webstack_site_group'
        verbose_name = '网站分组'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=255, verbose_name='名称')
    icon = models.CharField(max_length=255, default='linecons-star', verbose_name='图标')
    weight = models.IntegerField(default=1, verbose_name='权重')

    def __str__(self):
        return self.name


class Environment(BaseModel):
    class Meta:
        db_table = 'webstack_env'
        verbose_name = '网络环境'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=255, verbose_name="名称")

    def __str__(self):
        return self.name


class Site(BaseModel):
    class Meta:
        db_table = 'webstack_site'
        verbose_name = '网站'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=255, verbose_name='名称')
    description = models.CharField(max_length=255, verbose_name='描述')
    url = models.URLField(verbose_name='链接')
    title = models.CharField(max_length=255, verbose_name='原始标题')
    icon = models.URLField(verbose_name='站点图标',
                           default='https://aupicgo.oss-cn-shanghai.aliyuncs.com/img/20200910125957.ico')
    weight = models.IntegerField(verbose_name='网站权重', default=1)
    group = models.ForeignKey(SiteGroup, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name


class EnvWebsite(BaseModel):
    class Meta:
        db_table = 'webstack_env_site'
        verbose_name = '环境链接'
        verbose_name_plural = '环境链接'

    env = models.ForeignKey(Environment, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    url = models.URLField(verbose_name='链接')