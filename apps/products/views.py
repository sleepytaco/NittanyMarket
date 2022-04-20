from django.shortcuts import render, get_object_or_404

from apps.products.models import Category


def category(request, category_name):
    cat = get_object_or_404(Category, category_name=category_name)
    return render(request,
                  'products/category_page.html',
                  {'category': get_object_or_404(Category, category_name=category_name)})
