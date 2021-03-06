# Generated by Django 2.2 on 2021-10-31 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0002_auto_20211020_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='contactNumber',
            field=models.BigIntegerField(default=None),
        ),
    ]
