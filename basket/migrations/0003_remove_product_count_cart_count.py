# Generated by Django 4.0.4 on 2022-05-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_remove_cart_count_alter_product_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.AddField(
            model_name='cart',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Кол-во товара'),
        ),
    ]
