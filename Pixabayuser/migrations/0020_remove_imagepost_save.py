# Generated by Django 3.1.5 on 2021-01-26 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pixabayuser', '0019_auto_20210126_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='save',
        ),
    ]
