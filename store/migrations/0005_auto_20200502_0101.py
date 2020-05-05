# Generated by Django 2.2.7 on 2020-05-01 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200502_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordreritem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order'),
        ),
        migrations.AlterField(
            model_name='ordreritem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product'),
        ),
    ]
