# Generated by Django 4.1.3 on 2023-01-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_routine_routine_pdf_routine_marksheet_pdf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='marksheet_pdf',
        ),
        migrations.AddField(
            model_name='routine',
            name='routine_pdf',
            field=models.FileField(default=0, upload_to='media/files/routine'),
            preserve_default=False,
        ),
    ]
