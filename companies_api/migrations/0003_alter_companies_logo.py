# Generated by Django 3.2.16 on 2022-12-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies_api', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='logo',
            field=models.ImageField(max_length=255, null=True, upload_to='companies_logos'),
        ),
    ]
