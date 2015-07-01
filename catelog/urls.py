from django.conf.urls import patterns, url
from django.conf.urls.static import static
from ecomstore import settings

urlpatterns = patterns('catelog.views',
   (r'^$', 'index', {'template_name' : 'catelog/index.html'}, 'catelog_home'),
   (r'^category/(?P<category_slug>[\w\-]+)/$', 'category_page',
    {'template_name': 'catelog/category.html'}, 'catelog_category'),
   (r'^product/(?P<product_slug>[\w\-]+)/$', 'product_page', 
    {'template_name': 'catelog/product.html'}, 'catelog_product'),
   ) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
