# Generated by Django 3.2.16 on 2022-10-08 10:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='地址'),
            preserve_default=False,
        ),
    ]
