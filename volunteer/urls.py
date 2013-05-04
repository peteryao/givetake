from django.conf.urls import patterns, include, url

urlpatterns = patterns('volunteer.views',
    url(r'^$', 'index'),
)
