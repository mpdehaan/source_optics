# Generated by Django 2.2.2 on 2019-08-31 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0020_statistic_days_before_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='days_active',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistic',
            name='longevity',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
