# Generated by Django 3.1.5 on 2021-01-26 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pixabayuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='like',
        ),
        migrations.RemoveField(
            model_name='imagepost',
            name='save',
        ),
    ]
