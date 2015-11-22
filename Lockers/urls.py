from django.conf.urls import patterns, include, url
from django.contrib import admin

from GetNFC.views import vindex,vbox,vuser

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lockers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',vindex),
    url(r'^box/$',vbox),
    url(r'^user/$',vuser),
)
