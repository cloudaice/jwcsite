#@+leo-ver=5-thin
#@+node:cloudaice.20120216102454.1121: * @file /home/cloudaice/pyrepo/jwcsite/urls.py
#@@language python
#@@tabwidth -4
#@+others
#@+node:cloudaice.20120216102454.1122: ** urls declarations
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from jwcsite.stu_service import views
from jwcsite.stu_service import w_data
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jwcsite.views.home', name='home'),
    # url(r'^jwcsite/', include('jwcsite.foo.urls')),
    url(r'^$',views.home_page),
    url(r'^data/$',w_data.insertdata),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns+=staticfiles_urlpatterns()
#@-others
#@-leo
