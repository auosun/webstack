from rest_framework import serializers

from main.models import Website


class WebSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Website
        fields = "__all__"
