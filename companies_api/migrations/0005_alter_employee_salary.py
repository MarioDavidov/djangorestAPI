# Generated by Django 3.2.16 on 2022-12-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies_api', '0004_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]