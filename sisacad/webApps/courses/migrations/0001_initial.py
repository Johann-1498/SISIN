# Generated by Django 5.0.6 on 2024-06-09 22:10

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=7, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('theory_hours', models.DecimalField(decimal_places=2, max_digits=4)),
                ('credits', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hasLaboratory', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('year', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero'), (4, 'Cuarto'), (5, 'Quinto')], default=1)),
                ('semester', models.IntegerField(choices=[(1, 'Primer Semestre'), (2, 'Segundo Semestre'), (3, 'Tercer Semestre'), (4, 'Cuarto Semestre'), (5, 'Quinto Semestre'), (6, 'Sexto Semestre'), (7, 'Séptimo Semestre'), (8, 'Octavo Semestre'), (9, 'Noveno Semestre'), (10, 'Décimo Semestre')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('year', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero'), (4, 'Cuarto'), (5, 'Quinto')], default=1)),
                ('semester', models.IntegerField(choices=[(1, 'Primer Semestre'), (2, 'Segundo Semestre'), (3, 'Tercer Semestre'), (4, 'Cuarto Semestre'), (5, 'Quinto Semestre'), (6, 'Sexto Semestre'), (7, 'Séptimo Semestre'), (8, 'Octavo Semestre'), (9, 'Noveno Semestre'), (10, 'Décimo Semestre')], default=1)),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
