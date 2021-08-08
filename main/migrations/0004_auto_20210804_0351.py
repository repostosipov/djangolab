# Generated by Django 3.2.5 on 2021-08-03 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210804_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seller'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='main.Tag', verbose_name='тэги'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
