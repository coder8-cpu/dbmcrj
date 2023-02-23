# Generated by Django 4.1.3 on 2023-01-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_marksheets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='routine_pdf',
        ),
        migrations.AddField(
            model_name='routine',
            name='marksheet_pdf',
            field=models.FileField(default=0, upload_to='media/files/marksheets'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routine',
            name='roll',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
