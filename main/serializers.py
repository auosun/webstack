from django.db import models
from rest_framework import serializers

from main.models import EnvWebsite, Site, SiteGroup


class SiteListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        pass

    def to_representation(self, data):
        request = self.context["request"]
        env = request.query_params.get("env", "default")
        iterable = data.all() if isinstance(data, models.Manager) else data
        websites = EnvWebsite.objects.filter(env=env, site__in=data.all())

        return [
            self.child.to_representation(item) for item in iterable
        ]


class SiteSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.url

    class Meta:
        model = Site
        list_serializer_class = SiteListSerializer
        fields = "__all__"


class SiteGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteGroup
        fields = "__all__"
