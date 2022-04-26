import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from apps.products.models import Category, ProductListing


@login_required
def category(request, category_name):
    """
    Displays a page of all the product listings under the specified category
    """
    if category_name.lower() == "all":
        return render(request, 'products/category_home.html')
    cat = get_object_or_404(Category, category_name=category_name)
    prod_listings = cat.product_listings.all().filter(quantity__gt=0)
    return render(request,
                  'products/product_listings.html',
                  {'category': cat,
                   'product_listings': prod_listings})


@login_required
def create_product_listing(request):
    listing = request.POST
    print(listing)
    categories = Category.objects.all()
    if request.method == "POST":
        fields = ['title', 'product_name', 'product_description', 'price', 'quantity',
                  "category"]
        errors = []
        for field in fields:
            if (field == "category" and listing[field] == "Select A Category") or listing[field].strip() == "":
                errors.append(" ".join(field.split("_")).title())

        if errors:
            messages.error(request, f"Please fill in the following fields: " + ', '.join(errors))
        else:
            seller = request.user.seller_infos.first()
            listing_id = ProductListing.objects.count() + 1
            title = listing["title"]
            product_name = listing["product_name"]
            product_description = listing["product_description"]
            price = listing["price"] if "$" in listing["price"] else "$" + listing["price"]
            quantity = listing["quantity"]
            product_category = Category.objects.filter(category_name=listing["category"]).first()

            new_listing = ProductListing(seller=seller,
                                         listing_id=ProductListing.objects.count() + 1,
                                         title=title,
                                         product_name=product_name,
                                         product_description=product_description,
                                         price=price,
                                         quantity=quantity,
                                         category=product_category)
            new_listing.save()

            messages.success(request, "Successfully published your listing!")
            return redirect('product_listing', listing_id=listing_id)

    return render(request, 'products/create_product_listing.html', {"categories": categories, "listing": listing})


@login_required
def remove_product_listing(request, listing_id):
    if request.user.buyer_infos.exists():
        messages.error(request, "You must have a seller account type to perform this action.")
        return redirect('home')
    listing = ProductListing.objects.filter(listing_id=listing_id).first()
    if request.user.seller_infos.first() == listing.seller:
        listing.active_period = datetime.datetime.now().date()
        listing.save(update_fields=['active_period'])
        messages.success(request, "Successfully removed product listing.")
    else:
        messages.error(request, "You do not own that product listing.")
    return redirect('product_listings')


@login_required
def product_listings(request):
    if request.user.buyer_infos.exists():
        messages.error(request, "You must have a seller account type to view that page.")
        return redirect('home')
    listings = request.user.seller_infos.first().product_listings.all().filter(~Q(active_period=None))

    return render(request, 'products/product_listings_seller.html', {"listings": listings})


@login_required
def product_listing(request, listing_id):
    listing = get_object_or_404(ProductListing, listing_id=listing_id)
    if listing.active_period:
        messages.info(request, "Looks like that product listing was taken down by the seller :(")
        return redirect('product_listings')
    return render(request, 'products/product_listing.html', {"listing": listing})


@login_required
@require_POST
def search(request):
    listings = ProductListing.objects.filter(product_name__istartswith=request.POST["query"]) \
               | ProductListing.objects.filter(title__istartswith=request.POST["query"])
    return render(request, 'products/search.html', {"listings": listings.filter(quantity__gt=0)})
