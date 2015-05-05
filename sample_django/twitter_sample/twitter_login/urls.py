
from django.conf.urls import url, include
from django.contrib import admin

from twitter_login.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'home', home),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?$', t_login),
    url(r'^logout/?$', twitter_logout),
    url(r'^login/authenticated/?$', twitter_authenticated),
        ]
