from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login, logout

urlpatterns = patterns('volunteer.views',
    url(r'^$', 'index', name="index"),
    url(r'^listing/$', 'listing', name="listing"),
    url(r'^charities/$', 'charities', name="charity"),
    )

urlpatterns += patterns('volunteer.views', 
    url(r'^user/login/$', 'user_login', name="user_login"),
    )

urlpatterns += patterns('',
    url(r'^user/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
    url(r'^user/logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),
    )