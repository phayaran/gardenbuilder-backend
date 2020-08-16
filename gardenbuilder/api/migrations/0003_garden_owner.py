# Generated by Django 3.1 on 2020-08-15 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20200814_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gardens', to=settings.AUTH_USER_MODEL),
        ),
    ]