# Generated by Django 4.1.3 on 2023-01-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_admitcard_admit_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=1000)),
                ('semester', models.CharField(max_length=1000)),
                ('branch', models.CharField(max_length=1000)),
                ('exam_pdf', models.FileField(upload_to='media/files/admitcard')),
                ('course_type', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=1000)),
                ('semester', models.CharField(max_length=1000)),
                ('branch', models.CharField(max_length=1000)),
                ('notification_pdf', models.FileField(upload_to='media/files/admitcard')),
                ('course_type', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='admitcard',
            name='course_type',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marksheets',
            name='course_type',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='course_type',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routine',
            name='course_type',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdata',
            name='branch',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdata',
            name='course_type',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
