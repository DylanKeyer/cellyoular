from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'cellyoular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quote/', 'quote.views.index', name='quote'),
    url(r'^$', 'home.views.index', name='index'),
]
