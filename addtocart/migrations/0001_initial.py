# Generated by Django 2.2.5 on 2019-11-07 01:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manageUsers', '0001_initial'),
        ('manageStores', '0001_initial'),
        ('manageItems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_qty', models.PositiveIntegerField(default=1)),
                ('submitted_status', models.CharField(max_length=100)),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modify date')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageItems.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default=0)),
                ('customer_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Urgent', 'Urgent'), ('Invalid', 'Invalid'), ('Awaitting Processing', 'Awaitting Processing'), ('Transfer To Kitchen', 'Transfer To Kitchen'), ('Ready For Shipping', 'Ready For Shipping'), ('Delivered', 'Delivered')], default='Awaitting Processing', max_length=100)),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modify date')),
                ('cart', models.ManyToManyField(to='addtocart.Cart')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageStores.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageUsers.Customer')),
            ],
        ),
    ]
