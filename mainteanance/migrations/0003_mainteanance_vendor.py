# Generated by Django 4.2.1 on 2023-05-15 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('mainteanance', '0002_remove_mainteanance_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainteanance',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_mainteanance', to='vendor.vendor'),
            preserve_default=False,
        ),
    ]
