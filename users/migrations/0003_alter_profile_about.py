# Generated by Django 4.0.6 on 2022-07-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
