# Generated by Django 3.1.5 on 2021-01-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pixabayuser', '0018_auto_20210126_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='Title',
            field=models.CharField(max_length=30),
        ),
    ]
