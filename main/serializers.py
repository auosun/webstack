from django.db import models
from rest_framework import serializers

from main.models import EnvWebsite, Site, SiteGroup


class SiteListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        pass

    def to_representation(self, data):
        request = self.context["request"]
        env = request.query_params.get("env")
        iterable = data.all() if isinstance(data, models.Manager) else data
        self.context["env_site_url"] = {i.id: i.url for i in iterable}

        if env:
            websites = EnvWebsite.objects.filter(env=env, site__in=data.all())
            self.context["env_site_url"].update({web_site.site.id: web_site.url for web_site in websites})

        return [
            self.child.to_representation(item) for item in iterable
        ]


class SiteSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return self.context["env_site_url"].get(obj.id, obj.url)

    class Meta:
        model = Site
        list_serializer_class = SiteListSerializer
        fields = "__all__"


class SiteGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteGroup
        fields = "__all__"
