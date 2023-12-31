# Generated by Django 4.2.7 on 2023-11-09 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('brigade_number', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Locomotive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=255, unique=True)),
                ('depot', models.CharField(max_length=255)),
                ('locomotive_type', models.CharField(choices=[('cargo', 'Cargo'), ('passenger', 'Passenger')], max_length=10)),
                ('year_of_production', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_brigade_leader', models.BooleanField()),
                ('birth_date', models.DateField()),
                ('brigade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LMDA.brigade')),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_type', models.CharField(choices=[('current', 'Current'), ('maintenance', 'Maintenance'), ('unscheduled', 'Unscheduled')], max_length=12)),
                ('start_date', models.DateField()),
                ('days_required', models.IntegerField()),
                ('daily_repair_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brigade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LMDA.brigade')),
                ('locomotive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LMDA.locomotive')),
            ],
        ),
    ]
