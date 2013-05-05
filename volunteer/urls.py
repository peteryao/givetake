from django.conf.urls import patterns, include, url

urlpatterns = patterns('volunteer.views',
    url(r'^$', 'index', name="index"),
    url(r'^listing/$', 'listing', name="listing"),
    url(r'^charities/$', 'charities', name="charity"),
    )

urlpatterns += patterns('volunteer.views', 
    url(r'^user/login/$', 'user_login', name="user_login"),
    url(r'^user/logout/$', 'user_logout', name="user_logout"),
    )