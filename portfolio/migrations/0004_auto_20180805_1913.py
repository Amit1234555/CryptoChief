# Generated by Django 2.0.7 on 2018-08-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_position_price_purchased_usd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='price_purchased_usd',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
