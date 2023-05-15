# Generated by Django 4.2.1 on 2023-05-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=256)),
                ('service', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('phone_number', models.CharField(max_length=256)),
            ],
        ),
    ]