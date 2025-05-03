from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return ['website:index', 'website:about', 'website:contact']  # Add your static view names here

    def location(self, item):
        return reverse(item)  # Reverse the URL for the static view

