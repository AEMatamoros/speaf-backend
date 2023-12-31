# Generated by Django 4.2.7 on 2023-11-23 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('discount', models.IntegerField(null=True, verbose_name='Descuento')),
                ('category', models.CharField(choices=[('J', 'Jardineria'), ('L', 'Limpieza'), ('A', 'Autos'), ('H', 'Hogar'), ('C', 'Comida'), ('O', 'Otros')], default='O', max_length=5, verbose_name='Categoria')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='SellDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='bills.product')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, verbose_name='ClientName')),
                ('rtn', models.IntegerField(verbose_name='RTN')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sell_detail', models.ManyToManyField(related_name='sell_detail', to='bills.selldetail')),
            ],
        ),
    ]
