# Generated by Django 3.2.2 on 2021-05-23 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0010_cita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asistencia', models.IntegerField()),
                ('NSP', models.IntegerField()),
                ('usuario_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejemplo.paciente')),
            ],
        ),
    ]