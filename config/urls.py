from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

def easy(url_str):
    import re
    pattern = re.compile(r':\w+/?')
    matches = pattern.findall(url_str)
    for match in matches:
        var = match[1:-1]
        var_re = r'(?P<%s>.*)/'%var
        url_str = url_str.replace(match, var_re)
    url_str += '$'
    return url_str

urlpatterns = patterns('',
    url(r'^$', 'config.views.index', name='index'),
    # url(easy('^project/:id/'), 'project.foo.view_name'),

    url(r'^admin/', include(admin.site.urls)),
)
