# Generated by Django 4.0.4 on 2022-06-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0015_alter_cart_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_product',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
