# Generated by Django 4.1.3 on 2023-01-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_syllabus_notification_label'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='semester_admit',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='semester_marksheet',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='semester_registration',
        ),
        migrations.RemoveField(
            model_name='studentdata',
            name='semester_routine',
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='admit_pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/files/admitcard'),
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='branch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='course_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='roll',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='semester',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='examroutine',
            name='branch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='examroutine',
            name='course_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='examroutine',
            name='exam_pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/files/admitcard'),
        ),
        migrations.AlterField(
            model_name='examroutine',
            name='semester',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='examroutine',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='blood_group',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='branch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='course_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='registrationNo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='rollno',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='semester',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='marksheets',
            name='branch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='marksheets',
            name='course_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='marksheets',
            name='marksheet_pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/files/marksheets'),
        ),
        migrations.AlterField(
            model_name='marksheets',
            name='roll',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='marksheets',
            name='semester',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='marksheets',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registerrollno',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='branch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='course_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='registration_pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/files/registration'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='roll',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='semester',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='branch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='day',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='semester',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='subject',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='teacher',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='time',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='branch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='course_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='rollno',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='semester',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='Rollno',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='password',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
