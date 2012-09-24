from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^signup/$',
     'Accounts.views.signup',
         {'template_name': 'accounts/signup.html',
          'email_template_name': 'accounts/activationEmail.html'}),

    #robots
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),


    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('Accounts.urls')),
    url(r'^', include('Accounts.urls')),
)
