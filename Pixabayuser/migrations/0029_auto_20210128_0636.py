# Generated by Django 3.1.5 on 2021-01-28 06:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Pixabayuser', '0028_auto_20210128_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]