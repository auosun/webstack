from rest_framework import viewsets, filters

from main.models import SiteGroup, Site, Environment
from main.serializers import SiteSerializer, SiteGroupSerializer, EnvironmentSerializer


class SiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['weight', ]
    ordering = ['-weight']


class SiteGroupViewSet(viewsets.ModelViewSet):
    queryset = SiteGroup.objects.all()
    serializer_class = SiteGroupSerializer


class EnvViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
