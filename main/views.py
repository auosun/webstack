from rest_framework import viewsets

from main.models import SiteGroup, Site
from main.serializers import SiteSerializer, SiteGroupSerializer


class SiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class SiteGroupViewSet(viewsets.ModelViewSet):
    queryset = SiteGroup.objects.all()
    serializer_class = SiteGroupSerializer
