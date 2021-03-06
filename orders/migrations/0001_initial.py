# Generated by Django 2.2.2 on 2019-06-05 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_auto_20190604_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='nome')),
                ('last_name', models.CharField(max_length=60, verbose_name='sobrenome')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150, verbose_name='endereço')),
                ('postal_code', models.CharField(max_length=30, verbose_name='cep')),
                ('city', models.CharField(max_length=100, verbose_name='cidade')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='atualizado')),
                ('paid', models.BooleanField(default=False, verbose_name='pago')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='preço')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantidade')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
            ],
        ),
    ]
