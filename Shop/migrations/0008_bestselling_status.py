# Generated by Django 4.2.2 on 2023-10-14 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_bestselling'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestselling',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
