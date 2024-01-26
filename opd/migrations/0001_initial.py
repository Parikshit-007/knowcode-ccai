# Generated by Django 4.1.13 on 2024-01-24 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0006_auto_20231223_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultantDoctorReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('consultant_doctor_id', models.TextField()),
                ('performance_detais', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Depwisereport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OPD_REGISTER',
            fields=[
                ('visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('visit_date', models.DateField(auto_now_add=True)),
                ('ddepartment', models.CharField(max_length=20)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='RefDoctorReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('ref_doc_id', models.TextField()),
                ('Referrals_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OPDTOIPDTRANSFER',
            fields=[
                ('transfer_id', models.AutoField(primary_key=True, serialize=False)),
                ('ipd_admission_id', models.TextField()),
                ('admission_date', models.DateField()),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
        migrations.CreateModel(
            name='OPDPatientSummary',
            fields=[
                ('summary_id', models.AutoField(primary_key=True, serialize=False)),
                ('summary_details', models.TextField(blank=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='OPD_REPORT',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_details', models.TextField(blank=True)),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
        migrations.CreateModel(
            name='OPD_PRESCRIPTION',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('prescription_details', models.TextField(blank=True)),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
        migrations.CreateModel(
            name='OPD_Billing',
            fields=[
                ('billing_id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_detail', models.TextField(default=None)),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.opd_register')),
            ],
        ),
    ]
