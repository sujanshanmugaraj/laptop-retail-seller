# Generated by Django 4.2.6 on 2023-11-06 15:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='brand',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='model',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='processor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='ram',
            field=models.CharField(choices=[('4GB', '4 GB'), ('8GB', '8 GB'), ('16GB', '16 GB'), ('32GB', '32 GB')], default='4GB', max_length=5),
        ),
        migrations.AddField(
            model_name='feature',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='checkoutdetail',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('[0-9]{10}')]),
        ),
        migrations.AlterField(
            model_name='checkoutdetail',
            name='zipcode',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[0-9]{6}')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('[0-9]{10}')]),
        ),
    ]
