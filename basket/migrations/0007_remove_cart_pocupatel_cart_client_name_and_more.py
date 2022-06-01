# Generated by Django 4.0.4 on 2022-05-31 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_pokupatel_cart_pocupatel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='pocupatel',
        ),
        migrations.AddField(
            model_name='cart',
            name='client_name',
            field=models.CharField(default=123, max_length=50, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Pokupatel',
        ),
    ]