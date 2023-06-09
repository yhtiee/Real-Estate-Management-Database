# Generated by Django 4.2.1 on 2023-05-15 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0002_alter_property_expense_alter_property_tenant'),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainteanance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainteanance', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_mainteanance', to='property.property')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_mainteanance', to='vendor.vendor')),
            ],
        ),
    ]
