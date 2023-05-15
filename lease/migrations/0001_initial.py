# Generated by Django 4.2.1 on 2023-05-15 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
        ('property', '0002_alter_property_expense_alter_property_tenant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lease', models.CharField(max_length=256)),
                ('lease_start_date', models.DateField(max_length=256)),
                ('lease_end_date', models.DateField(max_length=256)),
                ('lease_amount', models.DecimalField(decimal_places=2, max_digits=256)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='property_lease', to='property.property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenant_lease', to='tenant.tenant')),
            ],
        ),
    ]
