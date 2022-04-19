from django.db import models
from ..users.models import Buyer, Seller


class CreditCard(models.Model):
    card_num = models.CharField(primary_key=True, max_length=255)
    card_code = models.IntegerField()
    expire_month = models.CharField(max_length=255)
    expire_year = models.IntegerField()
    card_type = models.CharField(max_length=255)
    owner = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="credit_cards")

    def get_card_num(self):
        return f"************{self.card_num[-4:]}"


class Order(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="transactions")
    listing_id = models.IntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="orders")
    date = models.CharField(max_length=255)
    quantity = models.IntegerField()
    payment = models.FloatField()
