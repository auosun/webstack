from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from main.models import Menu, Website
from main.serializers import WebSiteSerializer, MenuSerializer


class WebSiteView(viewsets.ReadOnlyModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebSiteSerializer


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

