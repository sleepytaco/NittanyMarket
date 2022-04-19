# Generated by Django 3.2.4 on 2022-03-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('parent_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('rating_desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.IntegerField()),
                ('review_desc', models.CharField(max_length=255)),
            ],
        ),
    ]
