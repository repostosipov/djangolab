# Generated by Django 3.2.5 on 2021-08-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_ads_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='tags',
            field=models.ManyToManyField(to='main.Tag', verbose_name='тэги'),
        ),
    ]
