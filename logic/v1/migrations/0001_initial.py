# Generated by Django 4.2.2 on 2023-07-04 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice', models.CharField(max_length=200)),
                ('years_of_experience', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('hospital_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('estimate_cost', models.DecimalField(decimal_places=0, max_digits=12)),
                ('city', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.city')),
                ('disease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.disease', verbose_name='disease')),
                ('related_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.doctor', verbose_name='related_doctor')),
                ('related_hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.hospital', verbose_name='related_hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_patient', to=settings.AUTH_USER_MODEL, verbose_name='related_user')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('verified_date', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=0, max_digits=12)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentRequestStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VizaStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Viza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateTimeField()),
                ('assigned_date', models.DateTimeField()),
                ('related_payment_request', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='v1.paymentrequest', verbose_name='related_payment_request')),
                ('related_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='related_user')),
                ('status', models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.vizastatus')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_date', models.DateTimeField(auto_created=True)),
                ('last_updated', models.DateTimeField()),
                ('related_documents', models.ManyToManyField(to='v1.document', verbose_name='related_documents')),
                ('related_package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.package', verbose_name='tr_related_package')),
                ('related_patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='v1.patient', verbose_name='tr_related_user')),
                ('related_viza', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='v1.viza')),
                ('status', models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.treatmentrequeststatus')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_of_experience', models.IntegerField(default=0)),
                ('cor_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='support_doc', to=settings.AUTH_USER_MODEL, verbose_name='related_user')),
            ],
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='related_treatment_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.treatmentrequest'),
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='status',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.paymentstatus'),
        ),
        migrations.AddField(
            model_name='package',
            name='requirements',
            field=models.ManyToManyField(to='v1.requirement', verbose_name='package_reqs'),
        ),
        migrations.AddField(
            model_name='document',
            name='related_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.requirement', verbose_name='related_reqs'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='related_hospitals',
            field=models.ManyToManyField(related_name='hospital_doc', to='v1.hospital', verbose_name='hospitals'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='related_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_doc', to=settings.AUTH_USER_MODEL, verbose_name='related_user'),
        ),
    ]