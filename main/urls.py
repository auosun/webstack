from django.urls import path

from main.views import WebSiteView, MenuView

website_list = WebSiteView.as_view({
    'get': 'list'
})

menu_list = MenuView.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', website_list),
    path('menu/', menu_list)
]
