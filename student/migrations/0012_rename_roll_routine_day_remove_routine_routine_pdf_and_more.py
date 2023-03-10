# Generated by Django 4.1.3 on 2023-01-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_studentdata_id_alter_studentsignup_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routine',
            old_name='roll',
            new_name='day',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='routine_pdf',
        ),
        migrations.AddField(
            model_name='routine',
            name='subject',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routine',
            name='teacher',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routine',
            name='time',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
