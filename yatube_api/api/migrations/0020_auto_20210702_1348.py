# Generated by Django 2.2.6 on 2021-07-02 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20210702_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Блогер'),
        ),
    ]
