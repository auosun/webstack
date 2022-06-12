from django.shortcuts import render

from main.models import Menu, Website


def index_view(request):
    menus = Menu.objects.all().order_by('-weight')
    websites = Website.objects.all().order_by('-weight')

    return render(request, 'index.html', {"menus": menus, "websites": websites})
