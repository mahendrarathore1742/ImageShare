# Generated by Django 3.1.5 on 2021-01-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pixabayuser', '0011_imagepost_save'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='like',
        ),
    ]
