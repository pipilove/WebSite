from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

from WebSite.VoteSite.VoteSite.views import hello, current_datetime, hours_ahead


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'VoteSite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url('^hello/$', hello),
                       ('^time/$', current_datetime),
                       (r'^time/plus/(\d{1,2})/$', hours_ahead),
                       )
