from apps.products.models import Category


def root_categories(request):
    return {"root_categories": Category.objects.filter(parent_category="Root")}