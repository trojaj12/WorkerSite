# Generated by Django 3.2 on 2021-04-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0006_auto_20210414_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
