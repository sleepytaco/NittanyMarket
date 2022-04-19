import django
import os

from django.contrib.auth.hashers import make_password

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NittanyMarket.settings")
django.setup()

import csv
from apps.users.models import *
from apps.payments.models import *
from apps.products.models import *
from django.contrib.auth.models import User

"""
This is the script for populating an empty database with the tables already created. Each of the chunks of `with` blocks
represent the population of an individual table.
NOTE: I have put a simple check to see if a database already contains the same number of entries as the csv dataset
"""

#### POPULATE USER TABLE ####
with open(r'dataset\Users.csv', newline='') as f:
    reader = csv.reader(f)
    users = list(reader)[1:]
    if len(users) + 1 == User.objects.count():
        print(f"-> Looks like Users table has already been populated! (Contains {User.objects.count()} rows)")
    else:
        print(f"-> Populating the Users table with {len(users)} new rows...", end="")
        for user in users:
            # make_password is a hashing algo provided by Django
            # Django requires username to be filled for its User table
            u = User(username=user[0], email=user[0], password=make_password(user[1]))
            u.save()
        print(" Successfully populated Users table!")

#### POPULATE ZIPCODE_INFO TABLE ####
with open(r'dataset\Zipcode_Info.csv', newline='') as f:
    reader = csv.reader(f)
    zipcode_infos = list(reader)[1:]
    if len(zipcode_infos) == ZipcodeInfo.objects.count():
        print(f"-> Looks like ZipcodeInfo table has already been populated! (Contains {ZipcodeInfo.objects.count()} rows)")
    else:
        print(f"-> Populating the ZipcodeInfo table with {len(zipcode_infos)} new rows...", end="")
        for zi in zipcode_infos:
            zip = ZipcodeInfo(zipcode=zi[0], city=zi[1], state_id=zi[2],
                              population=zi[3] if zi[3] != '' else 0,
                              density=zi[4] if zi[4] != '' else 0,
                              county_name=zi[5], timezone=zi[6])
            zip.save()
        print(" Successfully populated ZipcodeInfo table!")

#### POPULATE ADDRESS TABLE ####
with open(r'dataset\Address.csv', newline='') as f:
    reader = csv.reader(f)
    addresses = list(reader)[1:]
    if len(addresses) == Address.objects.count():
        print(f"-> Looks like Address table has already been populated! (Contains {Address.objects.count()} rows)")
    else:
        print(f"-> Populating the Address table with {len(addresses)} new rows...", end="")
        for address in addresses:
            zipcode_info = ZipcodeInfo.objects.get(zipcode=address[1])
            add = Address(address_id=address[0], zipcode=zipcode_info, street_num=address[2], street_name=address[3])
            add.save()
        print(" Successfully populated Address table!")

#### POPULATE BUYERS TABLE ####
with open(r'dataset\Buyers.csv', newline='') as f:
    reader = csv.reader(f)
    buyers = list(reader)[1:]
    if len(buyers) == Buyer.objects.count():
        print(f"-> Looks like Buyers table has already been populated! (Contains {Buyer.objects.count()} rows)")
    else:
        print(f"-> Populating the Buyers table with {len(buyers)} new rows...", end="")
        for buyer in buyers:
            user = User.objects.get(username=buyer[0])
            home_address = Address.objects.get(address_id=buyer[5])
            billing_address = Address.objects.get(address_id=buyer[6])
            b = Buyer(buyer_email=user, first_name=buyer[1], last_name=buyer[2], gender=buyer[3], age=buyer[4],
                      home_address_id=home_address, billing_address_id=billing_address)
            b.save()
        print(" Successfully populated Buyers table!")

#### POPULATE SELLER TABLE ####
with open(r'dataset\Sellers.csv', newline='') as f:
    reader = csv.reader(f)
    sellers = list(reader)[1:]
    if len(sellers) == Seller.objects.count():
        print(f"-> Looks like Seller table has already been populated! (Contains {Seller.objects.count()} rows)")
    else:
        print(f"-> Populating the Seller table with {len(sellers)} new rows...", end="")
        for seller in sellers:
            user = User.objects.get(username=seller[0])
            s = Seller(seller_email=user, routing_number=seller[1], account_number=seller[2], balance=seller[3])
            s.save()
        print(" Successfully populated Seller table!")

#### POPULATE LOCAL VENDOR TABLE ####
with open(r'dataset\Local_Vendors.csv', newline='') as f:
    reader = csv.reader(f)
    vendors = list(reader)[1:]
    if len(vendors) == LocalVendor.objects.count():
        print(f"-> Looks like LocalVendor table has already been populated! (Contains {LocalVendor.objects.count()} rows)")
    else:
        print(f"-> Populating the LocalVendor table with {len(vendors)} new rows...", end="")
        for vendor in vendors:
            seller = User.objects.get(username=vendor[0]).seller_infos.first()
            business_address = Address.objects.get(address_id=vendor[2])
            v = LocalVendor(vendor_email=seller, business_name=vendor[1], business_address_id=business_address, customer_service_num=vendor[3])
            v.save()
        print(" Successfully populated LocalVendor table!")

#### POPULATE CREDIT CARDS TABLE ####
with open(r'dataset\Credit_Cards.csv', newline='') as f:
    reader = csv.reader(f)
    cards = list(reader)[1:]
    if len(cards) == CreditCard.objects.count():
        print(f"-> Looks like CreditCard table has already been populated! (Contains {CreditCard.objects.count()} rows)")
    else:
        print(f"-> Populating the CreditCard table with {len(cards)} new rows...", end="")
        for card in cards:
            owner = User.objects.get(username=card[5]).buyer_infos.first()
            c = CreditCard(card_num=card[0], card_code=card[1], expire_month=card[2], expire_year=card[3],
                           card_type=card[4], owner=owner)
            c.save()
        print(" Successfully populated CreditCard table!")

#### POPULATE CATEGORIES TABLE ####
with open(r'dataset\Categories.csv', newline='') as f:
    reader = csv.reader(f)
    categories = list(reader)[1:]
    if Category.objects.count() > 0:
        print(f"-> Looks like Categories table has already been populated! (Contains {Category.objects.count()} rows)")
    else:
        print(f"-> Populating the Categories table with {len(categories)} new rows...", end="")
        for category in categories:
            c = Category(parent_category=category[0], category_name=category[1])
            c.save()
        print(" Successfully populated Categories table!")

#### POPULATE ORDERS TABLE ####
with open(r'dataset\Orders.csv', newline='') as f:
    reader = csv.reader(f)
    orders = list(reader)[1:]
    if len(orders) == Order.objects.count():
        print(f"-> Looks like Order table has already been populated! (Contains {Order.objects.count()} rows)")
    else:
        print(f"-> Populating the Order table with {len(orders)} new rows...", end="")
        for order in orders:
            seller = User.objects.get(username=order[1]).seller_infos.first()
            buyer = User.objects.get(username=order[3]).buyer_infos.first()
            o = Order(transaction_id=order[0], seller=seller, listing_id=order[2], buyer=buyer,
                      date=order[4], quantity=order[5], payment=order[6])
            o.save()
        print(" Successfully populated Order table!")

#### POPULATE PRODUCT LISTING TABLE ####
with open('dataset/Product_Listing.csv', newline='') as f:
    reader = csv.reader(f)
    listings = list(reader)[1:]
    if len(listings) == ProductListing.objects.count():
        print(
            f"-> Looks like ProductListing table has already been populated! (Contains {ProductListing.objects.count()} rows)")
    else:
        print(f"-> Populating the ProductListing table with {len(listings)} new rows...", end="")
        for listing in listings:
            category_name = listing[2].replace('and', '&') if 'and' in listing[2] else listing[2]
            try:
                category = Category.objects.get(category_name__iexact=category_name.title())
            except Exception as e:
                print("\nFailed to Insert Listing", listing)
                print("Failed to Find Category", category_name)
                print(e)
                break

            seller = User.objects.get(username=listing[0]).seller_infos.first()
            l = ProductListing(seller=seller, listing_id=listing[1], category=category, title=listing[3],
                               product_name=listing[4], product_description=listing[5], price=listing[6], quantity=listing[7])
            l.save()
        print(" Successfully populated ProductListing table!")

#### POPULATE REVIEW TABLE ####
with open(r'dataset\Reviews.csv', newline='') as f:
    reader = csv.reader(f)
    reviews = list(reader)[1:]
    if len(reviews) == Review.objects.count():
        print(f"-> Looks like Review table has already been populated! (Contains {Review.objects.count()} rows)")
    else:
        print(f"-> Populating the Review table with {len(reviews)} new rows...", end="")
        for review in reviews:
            buyer = User.objects.get(username=review[0]).buyer_infos.first()
            seller = User.objects.get(username=review[1]).seller_infos.first()
            r = Review(buyer=buyer, seller=seller, listing_id=review[2], review_desc=review[3])
            r.save()
        print(" Successfully populated Review table!")

#### POPULATE REVIEW TABLE ####
with open(r'dataset\Ratings.csv', newline='') as f:
    reader = csv.reader(f)
    ratings = list(reader)[1:]
    if len(ratings) == Rating.objects.count():
        print(f"-> Looks like Rating table has already been populated! (Contains {Rating.objects.count()} rows)")
    else:
        print(f"-> Populating the Rating table with {len(ratings)} new rows...", end="")
        for rating in ratings:
            buyer = User.objects.get(username=rating[0]).buyer_infos.first()
            seller = User.objects.get(username=rating[1]).seller_infos.first()
            r = Rating(buyer=buyer, seller=seller, date=rating[2], rating=rating[3], rating_desc=rating[4])
            r.save()
        print(" Successfully populated Rating table!")
