from django.conf.urls import patterns, include, url

from jackpot import views
from rest_framework.urlpatterns import format_suffix_patterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^all/$', views.articles),
    url(r'^bowlers/$', views.bowler_list),
    url(r'^bowler/(?P<pk>[0-9|A-Z|a-z]+)/$', views.bowler_detail),
    url(r'^leagues/$', views.league_list),
    url(r'^league/(?P<pk>[0-9|A-Z|a-z]+)/$', views.league_detail),
    url(r'^league/(?P<pk>[0-9|A-Z|a-z]+)/joinleague/$', views.join_league),
    #url(r'^create_bowler/$', views.create_bowler),
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
