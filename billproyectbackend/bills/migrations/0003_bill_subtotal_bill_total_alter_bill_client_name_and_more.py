# Generated by Django 4.2.7 on 2023-11-25 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_remove_bill_sell_detail_bill_selldetail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='subtotal',
            field=models.FloatField(blank=True, null=True, verbose_name='Subtotal'),
        ),
        migrations.AddField(
            model_name='bill',
            name='total',
            field=models.FloatField(blank=True, null=True, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='client_name',
            field=models.CharField(max_length=50, verbose_name='Nombre del Cliente'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='selldetail',
            field=models.ManyToManyField(blank=True, related_name='selldetail', to='bills.selldetail', verbose_name='Detalles de la venta'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('J', 'Jardineria'), ('L', 'Limpieza'), ('A', 'Autos'), ('H', 'Hogar'), ('C', 'Comida'), ('T', 'Tecnologia'), ('O', 'Otros')], default='O', max_length=5, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='selldetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion'),
        ),
        migrations.AlterField(
            model_name='selldetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='bills.product', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='selldetail',
            name='quantity',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
    ]
