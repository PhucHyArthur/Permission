# Generated by Django 4.2.16 on 2024-11-14 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_alter_company_company_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankingDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('holder_name', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_branch', models.CharField(max_length=255)),
                ('bank_number', models.IntegerField()),
                ('swift_code', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('tel', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representatives', to='supplier.bankingdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('tel', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('tax_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='supplier.bankingdetail')),
                ('representative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='supplier.representative')),
            ],
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='company',
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]