# Generated by Django 3.0.3 on 2020-03-09 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cementerio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('construccion', models.CharField(max_length=50)),
                ('lote', models.IntegerField()),
                ('lote_num', models.CharField(max_length=30)),
                ('lote_cuadro', models.CharField(max_length=30)),
                ('dimension', models.CharField(max_length=30)),
                ('precio_lote', models.FloatField()),
                ('vigencia', models.IntegerField()),
                ('caduca', models.DateTimeField(blank=True, null=True)),
                ('dias_concesion', models.IntegerField(default=30)),
                ('caduca_concesion', models.DateTimeField(blank=True, null=True)),
                ('dias_trabajo', models.IntegerField()),
                ('final_trabajo', models.DateTimeField(blank=True, null=True)),
                ('prorroga_iniciar', models.IntegerField(default=180)),
                ('fin_prorroga_iniciar', models.DateTimeField(blank=True, null=True)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('prorroga_trabajo', models.IntegerField(default=240)),
                ('fecha_final', models.DateTimeField(blank=True, null=True)),
                ('trabajo_final', models.NullBooleanField(default=False)),
                ('trabajo_final_fecha', models.DateTimeField(blank=True, null=True)),
                ('deuda_anual1', models.FloatField(default=0)),
                ('deuda_anual2', models.FloatField(default=0)),
                ('deuda_anual3', models.FloatField(default=0)),
                ('deuda_anual4', models.FloatField(default=0)),
                ('deuda_total', models.FloatField(editable=False)),
                ('abono_anual', models.FloatField()),
                ('fecha_anual1', models.DateTimeField(blank=True, null=True)),
                ('monto_anual1', models.FloatField(default=0)),
                ('fecha_anual2', models.DateTimeField(blank=True, null=True)),
                ('monto_anual2', models.FloatField(default=0)),
                ('fecha_anual3', models.DateTimeField(blank=True, null=True)),
                ('monto_anual3', models.FloatField(default=0)),
                ('fecha_anual4', models.DateTimeField(blank=True, null=True)),
                ('monto_anual4', models.FloatField(default=0)),
                ('contrato', models.ImageField(blank=True, null=True, upload_to='')),
                ('metro', models.FloatField(default=0)),
                ('precio_metro', models.FloatField(default=0)),
                ('total', models.FloatField(editable=False)),
                ('plano', models.NullBooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
        ),
    ]
