# Generated by Django 5.0.1 on 2024-01-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='country_code',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='information',
            name='flag',
            field=models.URLField(),
        ),
    ]