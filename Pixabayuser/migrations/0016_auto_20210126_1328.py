# Generated by Django 3.1.5 on 2021-01-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pixabayuser', '0015_auto_20210126_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
