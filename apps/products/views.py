from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from apps.products.models import Category, ProductListing


@login_required
def category(request, category_name):
    """
    Displays a page of all the product listings under the specified category
    """
    if category_name.lower() == "all":
        return render(request, 'products/category_home.html')
    category = get_object_or_404(Category, category_name=category_name)
    product_listings = category.product_listings.all().filter(quantity__gt=0)
    return render(request,
                  'products/product_listings.html',
                  {'category': category,
                   'product_listings': product_listings})


@login_required
def product_listings(request):
    if request.user.buyer_infos.exists():
        messages.error(request, "You must have a seller account type to view that page.")
        return redirect('home')
    return render(request, 'products/product_listings_seller.html')


@login_required
def product_listing(request, listing_id):
    listing = get_object_or_404(ProductListing, listing_id=listing_id)
    return render(request, 'products/product_listing.html', {"listing": listing})
