from django.db import models
from django.contrib.auth.models import User
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Bigender', 'Bigender'),
    ('Polygender', 'Polygender'),
    ('Non-binary', 'Non-binary'),
    ('Agender', 'Agender'),
    ('Genderfluid', 'Genderfluid'),
    ('Genderqueer', 'Genderqueer')
)


# class User(models.Model):
#     email = models.CharField(primary_key=True, max_length=255)
#     password = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.email


class ZipcodeInfo(models.Model):
    zipcode = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=255)
    state_id = models.CharField(max_length=255)
    population = models.IntegerField()
    density = models.FloatField()
    county_name = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)

    def __str__(self):
        return str(self.zipcode)


class Address(models.Model):
    address_id = models.CharField(primary_key=True, max_length=255)
    zipcode = models.ForeignKey(ZipcodeInfo, on_delete=models.CASCADE)
    street_num = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)

    def __str__(self):
        return self.address_id


# Buyer -> User
# LocalVendor -> Seller -> User
#
# where:
# -> is foreign key for email field

class Buyer(models.Model):
    buyer_email = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, related_name="buyer_infos")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    age = models.IntegerField()
    home_address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="home_address")
    billing_address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="billing_address")

    def __str__(self):
        return str(self.buyer_email)


class Seller(models.Model):
    seller_email = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, related_name="seller_infos")
    # email = models.CharField(primary_key=True, max_length=255)
    routing_number = models.CharField(max_length=255)
    account_number = models.IntegerField()
    balance = models.FloatField()

    def __str__(self):
        return str(self.seller_email)


class LocalVendor(models.Model):
    vendor_email = models.ForeignKey(Seller, on_delete=models.CASCADE, primary_key=True, related_name="vendor_infos")
    # email = models.CharField(primary_key=True, max_length=255)
    business_name = models.CharField(max_length=255)
    business_address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name="business_address", null=True)
    customer_service_num = models.CharField(max_length=255)

    def __str__(self):
        return self.business_name

