from cart.models import CartItem
from catelog.models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

import decimal, random

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for h in range(cart_id_length):
        cart_id += chars[random.randint(0, len(chars)-1)]
    return cart_id

def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    postdata = request.POST.copy()
    product_slug = postdata.get('product_slug', '')
    quantity = postdata.get('quantity', 1)
    p = get_object_or_404(Product, slug=product_slug)
    cart_products = get_cart_items(request)
    product_in_cart = False
    for item in cart_products:
        if item.product.id == p.id:
            item.augment_quantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)
        ci.save()

def cart_item_count(request):
    return get_cart_items(request).count()

def get_single_item(request, item_id):
    return get_object_or_404(CartItem, id=item_id, cart_id=_cart_id(request))
        
def remove_from_cart(request):
    postdata = request.POST.copy()
    item_id = postdata.get('item_id')
    cart_item = get_single_item(request, item_id)
    if cart_item:
        cart_item.delete()

def update_cart(request):
    postdata = request.POST.copy()
    item_id = postdata.get('item_id') 
    quantity = postdata.get('quantity')
    cart_item = get_single_item(request, item_id)
    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request)

def cart_subtotal(request):
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        cart_total += cart_item.product.price * cart_item.quantity
    return cart_total

def get_distinct_item(request):
    return get_cart_items(request).count()

