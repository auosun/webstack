from django.contrib import admin

from .models import Environment, EnvWebsite, Site, SiteGroup


@admin.register(SiteGroup)
class SiteGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'weight')
    list_editable = ['icon', 'weight']


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_filter = ['group']
    list_display = ('name', 'description', 'url', 'weight', 'group')
    list_editable = ['description', 'url', 'weight', 'group']


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    pass


@admin.register(EnvWebsite)
class EnvSiteAdmin(admin.ModelAdmin):
    list_display = ('env', 'site', 'url')
