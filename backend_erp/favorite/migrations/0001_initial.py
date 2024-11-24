# Generated by Django 4.2.16 on 2024-11-14 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0003_finishedproducts_location_rack_rawmaterials_and_more'),
        ('db_diy', '0002_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_diy.clients')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('favorites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_lines', to='favorite.favorites')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.finishedproducts')),
            ],
        ),
    ]
