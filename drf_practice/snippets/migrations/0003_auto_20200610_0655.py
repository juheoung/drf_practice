# Generated by Django 3.0.7 on 2020-06-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20200610_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
