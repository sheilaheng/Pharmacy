# Generated by Django 3.0.5 on 2023-08-03 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwambokadjangoProject', '0002_remove_drug_batchnum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='name',
            new_name='drug',
        ),
    ]
