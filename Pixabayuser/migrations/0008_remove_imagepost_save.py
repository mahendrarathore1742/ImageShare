# Generated by Django 3.1.5 on 2021-01-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pixabayuser', '0007_auto_20210126_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='save',
        ),
    ]
