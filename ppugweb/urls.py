import os

from django.contrib import admin
from django.conf.urls.defaults import *
from django.conf import settings
from zinnia.sitemaps import TagSitemap, EntrySitemap, CategorySitemap, AuthorSitemap
import zinnia

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.simple.redirect_to', 
                        {'url': '/blog/'}),
                       url(r'^blog/',           include('zinnia.urls')),
                       url(r'^comments/',       include('django.contrib.comments.urls')),
                       url(r'^xmlrpc/$',        'django_xmlrpc.views.handle_xmlrpc'),
                       url(r'^i18n/',           include('django.conf.urls.i18n')),
                       url(r'^admin/doc/',      include('django.contrib.admindocs.urls')),
                       url(r'^admin/',          include(admin.site.urls)),
                       )

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns += patterns('django.contrib.sitemaps.views',
                        (r'^sitemap.xml$', 'index',
                         {'sitemaps': sitemaps}),
                        (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
                         {'sitemaps': sitemaps}),
                        )

# URLs to static media
# comment these when in production and should be aliased at the webserver
# see settings.py
#       ZINNIA_MEDIA_URL
#       PPUGWEB_MEDIA_URL
urlpatterns += patterns('django.views.static',
                        url(r'^zinnia/(?P<path>.*)$', 'serve',
                            {'document_root': os.path.join(os.path.dirname(zinnia.__file__), 'media', 'zinnia')}),
                        url(r'^uploads/(?P<path>.*)$', 'serve',
                            {'document_root': os.path.join(os.path.dirname(__file__), 'uploads')}),
                        url(r'^skin-media/(?P<path>.*)$', 'serve',
                            {'document_root': os.path.join(os.path.dirname(__file__), 'skins', settings.PPUGWEB_SKIN, 'media')}),
                        )
