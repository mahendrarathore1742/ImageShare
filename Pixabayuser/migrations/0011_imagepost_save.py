# Generated by Django 3.1.5 on 2021-01-26 13:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pixabayuser', '0010_remove_imagepost_save'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='save',
            field=models.ManyToManyField(blank=True, related_name='post_save', to=settings.AUTH_USER_MODEL),
        ),
    ]
