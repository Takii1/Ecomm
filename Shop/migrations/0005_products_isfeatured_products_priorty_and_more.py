# Generated by Django 4.2.2 on 2023-10-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_home_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='isFeatured',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='priorty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_sale_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sub_categories',
            name='isFeautred',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sub_categories',
            name='setPriorty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sub_categories',
            name='status',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_status',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
