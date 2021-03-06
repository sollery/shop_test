# Generated by Django 4.0.4 on 2022-05-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='count',
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Кол-во товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=1, verbose_name='Цена'),
        ),
    ]
