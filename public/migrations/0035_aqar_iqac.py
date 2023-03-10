# Generated by Django 4.1.3 on 2023-02-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0034_delete_admissionquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='AQAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=1000, null=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='IQAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desgination', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='media/pics/administrative')),
            ],
        ),
    ]
