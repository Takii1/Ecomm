# Generated by Django 4.2.2 on 2023-10-06 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_alter_sub_categories_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='Shop.products'),
        ),
    ]
