from django.db import models
from rest_framework import serializers

from main.models import Website, Menu, EnvWebsite


class WebSiteListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        pass

    def to_representation(self, data):
        request = self._context["request"]
        env = request.query_params.get("env", "default")
        iterable = data.all() if isinstance(data, models.Manager) else data
        websites = EnvWebsite.objects.filter(env_id=env, site__in=data.all())

        return [
            self.child.to_representation(item) for item in iterable
        ]


class WebSiteSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.url

    class Meta:
        model = Website
        list_serializer_class = WebSiteListSerializer
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
