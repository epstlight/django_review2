# Generated by Django 2.2.6 on 2019-10-22 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_auto_20191018_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content2',
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
