# Generated by Django 3.2 on 2021-04-08 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('work_report', '0002_auto_20210408_0817'),
        ]

    operations = [
        migrations.AlterField(
                model_name='workreport',
                name='arrival',
                field=models.DateTimeField(null=True),
                ),
        migrations.AlterField(
                model_name='workreport',
                name='departure',
                field=models.DateTimeField(null=True),
                ),
        ]
