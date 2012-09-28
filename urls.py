from django.conf.urls.defaults import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead

urlpatterns = patterns('',
  ('^hello/$', hello),
  ('^time/$', current_datetime),
  (r'^time/plus/(\d{1,2})/$', hours_ahead),
)

