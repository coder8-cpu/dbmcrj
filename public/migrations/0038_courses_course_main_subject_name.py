# Generated by Django 4.1.3 on 2023-02-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0037_departments_eresources_departmentsfaculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_main_subject_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]