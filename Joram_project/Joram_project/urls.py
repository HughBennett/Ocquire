from django.conf.urls import patterns, include, url
from Ocquire import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Joram_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^admin/', include(admin.site.urls)),
     url(r'^$',views.index, name='index'),
)