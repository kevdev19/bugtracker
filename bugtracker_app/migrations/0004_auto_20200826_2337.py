# Generated by Django 3.0.9 on 2020-08-26 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugtracker_app', '0003_auto_20200826_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='createdby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
