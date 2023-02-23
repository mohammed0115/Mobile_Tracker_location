# Generated by Django 3.2 on 2023-02-22 19:11

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, max_length=255, null=True)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('results_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50)),
                ('IMEMI', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('network', models.CharField(max_length=15)),
                ('version', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=70)),
                ('region', models.CharField(max_length=70)),
                ('region_code', models.CharField(max_length=7)),
                ('country', models.CharField(max_length=7)),
                ('country_name', models.CharField(max_length=70)),
                ('country_code', models.CharField(max_length=7)),
                ('country_code_iso3', models.CharField(max_length=7)),
                ('country_capital', models.CharField(max_length=70)),
                ('country_tld', models.CharField(max_length=7)),
                ('continent_code', models.CharField(max_length=4)),
                ('in_eu', models.BooleanField()),
                ('postal', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=70)),
                ('utc_offset', models.CharField(max_length=10)),
                ('country_calling_code', models.CharField(max_length=7)),
                ('currency', models.CharField(max_length=10)),
                ('currency_name', models.CharField(max_length=40)),
                ('languages', models.CharField(max_length=100)),
                ('country_area', models.CharField(max_length=40)),
                ('asn', models.CharField(max_length=20)),
                ('org', models.CharField(max_length=20)),
                ('country_population', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
