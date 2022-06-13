from django.urls import path

from main.views import WebSiteView

website_list = WebSiteView.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', website_list),
]
