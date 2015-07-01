from django.shortcuts import render, render_to_response, get_object_or_404
from catelog.models import Category, Product
from django.template import RequestContext

def index(request, template_name='catelog/index.html'):
    page_title = 'Modern books and its infromation'
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def category_page(request, category_slug, template_name='catelog/category.html'):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(), 
            context_instance=RequestContext(request))

def product_page(request, product_slug, template_name='catelog/product.html'):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render_to_response(template_name, locals(),
            context_instance = RequestContext(request))
