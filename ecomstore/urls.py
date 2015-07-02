from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catelog.urls')), 
    url(r'^music/', include('music.urls'), name='music'),
    url(r'^cart/', include('cart.urls')),
]
