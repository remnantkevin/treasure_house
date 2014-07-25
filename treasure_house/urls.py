from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treasure_house.views.home', name='home'),

    url(r'^words/', include('words.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
