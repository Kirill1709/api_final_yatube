# Generated by Django 2.2.6 on 2021-06-25 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210625_1520'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='group',
            name='unique_group',
        ),
    ]