# Generated by Django 3.2.5 on 2021-08-01 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='seller',
            new_name='user',
        ),
    ]
