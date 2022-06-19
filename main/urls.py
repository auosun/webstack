from django.urls import path

from main.views import SiteViewSet, SiteGroupViewSet

site_list = SiteViewSet.as_view({
    'get': 'list'
})

group_list = SiteGroupViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', site_list),
    path('menu/', group_list)
]
