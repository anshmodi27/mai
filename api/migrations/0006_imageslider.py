# Generated by Django 3.2.8 on 2024-01-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='slider/')),
                ('image2', models.ImageField(upload_to='slider/')),
                ('image3', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]
