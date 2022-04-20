from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from apps.products.models import Category


@login_required
def category(request, category_name):
    """
    Displays a page of all the product listings under the specified category
    """
    return render(request,
                  'products/product_listings.html',
                  {'category': get_object_or_404(Category, category_name=category_name)})


@login_required
def product_listings(request):
    if request.user.buyer_infos.exists():
        messages.error(request, "You must have a seller account type to view that page.")
        return redirect('home')
    return render(request, 'products/product_listings_seller.html')
