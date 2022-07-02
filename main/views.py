from rest_framework import viewsets, filters
from rest_framework.response import Response

from base.viewset import HttpFuncViewSet
from main.handler import WebSiteHandler
from main.models import SiteGroup, Site, Environment
from main.serializers import SiteSerializer, SiteGroupSerializer, EnvironmentSerializer


class SiteViewSet(HttpFuncViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['weight', ]
    ordering = ['-weight']
    handler = WebSiteHandler

    def quick_create(self, request, *args, **kwargs):
        url = self.payload_get('url')
        group = self.payload_get('group_id')
        obj = self.handler.quick_create(url, group)
        if not obj:
            return Response({"message": "error"})

        return Response({"message": "ok"})


class SiteGroupViewSet(viewsets.ModelViewSet):
    queryset = SiteGroup.objects.all()
    serializer_class = SiteGroupSerializer


class EnvViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
