from django.shortcuts import render
from rest_framework import viewsets

from main.models import Menu, Website
from main.serializers import WebSiteSerializer


class WebSiteView(viewsets.ReadOnlyModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebSiteSerializer


def index_view(request):
    menus = Menu.objects.all().order_by('-weight')
    websites = Website.objects.all().order_by('-weight')

    return render(request, 'index.html', {"menus": menus, "websites": websites})
