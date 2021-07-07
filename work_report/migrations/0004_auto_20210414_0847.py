# Generated by Django 3.2 on 2021-04-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0003_auto_20210408_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workreport',
            name='arrival',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='creat_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='departure',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='workreport',
            name='description',
            field=models.TextField(),
        ),
    ]
