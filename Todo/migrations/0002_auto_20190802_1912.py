# Generated by Django 2.2.3 on 2019-08-03 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='completed',
            field=models.BooleanField(verbose_name=False),
        ),
    ]
