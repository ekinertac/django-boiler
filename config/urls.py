from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'config.views.index', name='index'),
    # url(r'^project/', include('project.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
