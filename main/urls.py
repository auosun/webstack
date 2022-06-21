from django.urls import path

from main.views import SiteViewSet, SiteGroupViewSet, EnvViewSet

site_list = SiteViewSet.as_view({
    'get': 'list'
})

group_list = SiteGroupViewSet.as_view({
    'get': 'list'
})

env_list = EnvViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', site_list),
    path('menu/', group_list),
    path('env/', env_list),
]
