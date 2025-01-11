from django.shortcuts import render ,get_object_or_404
from .cart import Cart 
from shop.models import Product
from django.http import JsonResponse


def cart_summery(request):
    return render(request, 'cart_summery.html', {})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action')=='post':
        Product_id = int(request.POST.get('Product_id'))
        Product=get_object_or_404(Product, id= Product_id)
        cart.add(Product=Product)

        response= JsonResponse({'Product name': Product.name})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
