# Generated by Django 4.1.3 on 2023-01-16 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_admitcard_registration_studentdata_semester_admit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admitcard',
            name='admit_pdf',
            field=models.FileField(upload_to='media/files/admitcard'),
        ),
    ]