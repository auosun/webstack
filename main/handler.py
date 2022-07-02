import os.path
import re
import typing

import requests
from bs4 import BeautifulSoup
from rest_framework import exceptions

from main.models import Site


class CollectWebSite(object):
    meta_keys = ('name', 'desc')

    def __init__(self, url, **kwargs):
        self.url = url
        self.content = dict(**kwargs)
        self._soup: typing.Optional[BeautifulSoup] = None

    def request_text(self):
        web_response = requests.get(self.url)
        if web_response.status_code != 200:
            raise exceptions.NotFound("无法获取到 %s 网页内容" % web_response.url)

        return web_response.text

    def _get_meta(self):
        meta = self.content.get('meta')
        if not meta:
            meta = self._soup.findAll('meta') or []
            self.content["meta"] = meta

        return meta

    def _get_key_meta(self, key):
        metas = self._get_meta()
        for meta in metas:
            if meta.get("name") == key or meta.get("id") == key:
                return meta

        return None

    def set_title(self):
        title = self._soup.find('title').text
        title = title or self.content.get('title') or 'default'
        setattr(self, 'title', title)

    def set_meta_keys(self):
        for key in self.meta_keys:
            value = self._get_key_meta(key) or "default"
            if value == 'default' and key == 'name':
                value = self.title

            setattr(self, key, value)

    def set_icon(self):
        links = self._soup.findAll('link') or []
        icon = None
        for link in links:
            if link.get("rel") in [['icon'], ['apple-touch-icon']]:
                if icon is None:
                    icon = link

                regex_size = re.compile(r"(?P<size>\d{1,4})x\d{1,4}")
                link_size = regex_size.match(link.get("sizes", "8x8")).groupdict().get("size", 0)
                icon_size = regex_size.match(icon.get("sizes", "8x8")).groupdict().get("size", 0)
                if link_size >= icon_size:
                    icon = link

        if not icon:
            return

        icon_link = icon.get("href")
        setattr(self, "icon", icon_link if icon_link.startswith("http") else os.path.join(self.url, icon_link))

    def collect(self):
        self._soup = BeautifulSoup(self.request_text(), 'html.parser')
        self.set_title()
        self.set_meta_keys()
        self.set_icon()
        return self


class WebSiteHandler(object):
    model = Site

    @classmethod
    def quick_create(cls, url, group_id):
        site = CollectWebSite(url).collect()
        site_obj = dict(url=url, name=site.name, title=site.title, description=site.desc, group_id=group_id)
        if hasattr(site, "icon"):
            site_obj.update(icon=site.icon)
        obj = cls.model.objects.create(
            **site_obj
        )
        return obj
