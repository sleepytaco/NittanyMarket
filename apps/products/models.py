from django.db import models
from ..users.models import Buyer, Seller


class Category(models.Model):
    category_name = models.CharField(max_length=255, primary_key=True)
    parent_category = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    def get_parents(self):
        """
        Returns a list of parent categories for a given category
        """
        stack = [self]
        tree = [self.category_name]
        while len(stack) != 0:
            current = stack.pop()
            if not current.parent_category == "Root":
                tree = [current.parent_category] + tree
                stack.append(Category.objects.get(category_name=current.parent_category))
        return tree

    def get_children(self):
        """
        Returns a list of parent categories for a given category
        """
        return Category.objects.filter(parent_category=self.category_name)


class ProductListing(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product_listings")
    listing_id = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="product_listings")
    title = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.IntegerField()
    active_period = models.DateField(null=True)

    def __str__(self):
        return f"Product Listing #{self.listing_id}: {self.title}"


class Review(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="reviews")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product_reviews")
    listing = models.ForeignKey(ProductListing, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review_desc = models.CharField(max_length=255)


class Rating(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="ratings")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product_ratings")
    date = models.CharField(max_length=255)
    rating = models.IntegerField()
    rating_desc = models.CharField(max_length=255)
