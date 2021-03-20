# Generated by Django 3.1.5 on 2021-01-26 13:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pixabayuser', '0012_remove_imagepost_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='save',
        ),
        migrations.AddField(
            model_name='imagepost',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
