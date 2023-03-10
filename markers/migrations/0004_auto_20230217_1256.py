# Generated by Django 3.2 on 2023-02-17 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('markers', '0003_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marker',
            name='name',
        ),
        migrations.AddField(
            model_name='marker',
            name='asn',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='city',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='continent_code',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_area',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_calling_code',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_capital',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_code',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_code_iso3',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_name',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_population',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='country_tld',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='currency',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='currency_name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='in_eu',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='ip',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='languages',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='network',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='org',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='postal',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='region',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='region_code',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='timezone',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='utc_offset',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='version',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
