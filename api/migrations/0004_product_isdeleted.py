# Generated by Django 3.2.8 on 2023-12-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_product_listdes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
