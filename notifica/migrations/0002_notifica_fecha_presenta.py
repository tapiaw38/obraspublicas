# Generated by Django 3.0.3 on 2020-02-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifica',
            name='fecha_presenta',
            field=models.DateField(blank=True, null=True),
        ),
    ]