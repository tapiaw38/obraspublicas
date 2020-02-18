# Generated by Django 3.0.3 on 2020-02-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('direccion', models.CharField(max_length=50, verbose_name='dirección')),
                ('profesion', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=50)),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
