# Generated by Django 3.2.4 on 2021-06-17 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0004_auto_20210207_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
    ]
