# Generated by Django 4.2.2 on 2023-09-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_categories',
            name='deleted_at',
            field=models.DateField(null=True),
        ),
    ]
