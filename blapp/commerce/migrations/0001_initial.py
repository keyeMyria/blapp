# Generated by Django 2.0.6 on 2018-06-08 10:33

import blapp.utils.db_fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', blapp.utils.db_fields.PrimaryKeyUUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', blapp.utils.db_fields.NameField(max_length=256, verbose_name='name')),
                ('description', blapp.utils.db_fields.DescriptionField(blank=True, verbose_name='description')),
                ('price', blapp.utils.db_fields.MoneyDecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', blapp.utils.db_fields.PrimaryKeyUUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid1, help_text='Unique ID used to ensure that offline clients can sync multiple times without creating duplicates. Offline clients *must* supply this.', unique=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='timestamp')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person', verbose_name='person')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'purchase',
                'verbose_name_plural': 'purchases',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='SalePoint',
            fields=[
                ('id', blapp.utils.db_fields.PrimaryKeyUUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', blapp.utils.db_fields.NameField(max_length=256, verbose_name='name')),
                ('description', blapp.utils.db_fields.DescriptionField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='sale_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.SalePoint', verbose_name='sale point'),
        ),
    ]
