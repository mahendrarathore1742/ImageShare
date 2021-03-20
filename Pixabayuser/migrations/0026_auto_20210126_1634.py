# Generated by Django 3.1.5 on 2021-01-26 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pixabayuser', '0025_auto_20210126_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='user',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
