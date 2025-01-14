# Generated by Django 2.2.1 on 2019-09-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0008_auto_20190913_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.TextField(blank=True, help_text='for github/gitlab imports', null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repos', to='source_optics.Organization'),
        ),
    ]
