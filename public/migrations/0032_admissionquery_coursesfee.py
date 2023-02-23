# Generated by Django 4.1.3 on 2023-01-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0031_documentrequired'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CoursesFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(blank=True, max_length=100, null=True)),
                ('coursefee', models.CharField(blank=True, max_length=30, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
