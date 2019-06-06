from django.conf.urls import include, url

from .v3.languages import languages
from .v3.sites import sites, pushnew
from .v3.push_notifications import sent_push_notifications

urlpatterns = [
    url(r'sites/$', sites, name='sites'),
    url(r'sites/pushnew/$', pushnew, name='pushnew'),
    url(r'sent_push_notifications/$', sent_push_notifications, name='sent_push_notifications'),
    url(r'(?P<site_slug>[-\w]+)/', include([
        url(r'languages$', languages),
    ])),
]
