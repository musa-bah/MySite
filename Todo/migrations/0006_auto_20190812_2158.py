# Generated by Django 2.2.1 on 2019-08-12 21:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0005_auto_20190812_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(default='0', null=True, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]