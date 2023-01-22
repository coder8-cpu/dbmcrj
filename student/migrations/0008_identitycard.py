# Generated by Django 4.1.3 on 2023-01-17 05:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_examroutine_notification_admitcard_course_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentityCard',
            fields=[
                ('id', models.BigAutoField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=1000)),
                ('rollno', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('semester', models.CharField(max_length=1000)),
                ('branch', models.CharField(max_length=1000)),
                ('course_type', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('blood_group', models.CharField(max_length=1000)),
                ('registrationNo', models.CharField(max_length=1000)),
            ],
        ),
    ]