from django.conf.urls.defaults import *
from potpiebear.ppbapp.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^potpiebear/', include('potpiebear.foo.urls')),
    url(r'^$', main),
    url(r'^home/$', main),
    url(r'^heart/$', heart),
    #url(r'^/hey/', include('potpiebear.ppbapp.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
#http://www.wolframalpha.com/input/?i=x%3D16+sin^3+t%2C+y%3D13+cos+t+-+5+cos%282t%29+-+2+cos%283t%29+-+cos%284t%29