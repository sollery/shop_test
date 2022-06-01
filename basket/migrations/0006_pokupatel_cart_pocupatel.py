# Generated by Django 4.0.4 on 2022-05-31 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokupatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='pocupatel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basket.pokupatel'),
            preserve_default=False,
        ),
    ]