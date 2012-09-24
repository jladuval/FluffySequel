from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',

    #robots
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),


    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'', 'Home.views.index')
)
