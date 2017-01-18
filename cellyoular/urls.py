from django.conf.urls import include, url
from django.contrib import admin
import home.views
import quote.views
import about.views
import register.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'cellyoular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quote/', quote.views.add_phone, name='quote'),
    url(r'^$', home.views.index, name='index'),
    url(r'^about/', about.views.index, name = 'about'),
    url(r'^register/$', register.views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', register.views.login, name='login'), # ADD NEW PATTERN!


]
