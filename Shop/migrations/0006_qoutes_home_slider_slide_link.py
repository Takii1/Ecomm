# Generated by Django 4.2.2 on 2023-10-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_products_isfeatured_products_priorty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qoute', models.TextField()),
                ('auther', models.CharField(max_length=55)),
                ('forDate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='home_slider',
            name='slide_link',
            field=models.TextField(null=True),
        ),
    ]
