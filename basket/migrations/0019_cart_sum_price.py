# Generated by Django 4.0.4 on 2022-06-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0018_remove_cart_order_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sum_price',
            field=models.PositiveIntegerField(default=1, verbose_name='Сумма'),
        ),
    ]
