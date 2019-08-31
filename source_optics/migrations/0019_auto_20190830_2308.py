# Generated by Django 2.2.2 on 2019-08-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0018_auto_20190810_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='color',
        ),
        migrations.AddField(
            model_name='statistic',
            name='days_since_seen',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='earliest_commit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='latest_commit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='interval',
            field=models.TextField(choices=[('DY', 'Day'), ('WK', 'Week'), ('MN', 'Month'), ('LF', 'Lifetime')], max_length=5),
        ),
    ]