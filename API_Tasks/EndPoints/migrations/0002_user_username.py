# Generated by Django 3.0.8 on 2020-08-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EndPoints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=255, unique=True, verbose_name='username'),
        ),
    ]
