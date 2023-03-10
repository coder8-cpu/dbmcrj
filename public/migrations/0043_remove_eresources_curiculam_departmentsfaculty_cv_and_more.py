# Generated by Django 4.1.3 on 2023-02-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0042_currentyear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eresources',
            name='curiculam',
        ),
        migrations.AddField(
            model_name='departmentsfaculty',
            name='cv',
            field=models.FileField(null=True, upload_to='media/deparments/cv'),
        ),
        migrations.AddField(
            model_name='eresources',
            name='Resource_link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='eresources',
            name='honours_resources_label',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='eresources',
            name='program_resources_label',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
